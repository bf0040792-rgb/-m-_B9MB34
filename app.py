from flask import Flask, render_template_string, request, jsonify
import time

app = Flask(__name__)

# ==========================================
# HTML INTERFACE (Design)
# ==========================================
HTML_CODE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OTP Tester (UI Demo)</title>
    <style>
        body {
            background-color: #0f0f0f;
            color: #00ff41;
            font-family: 'Courier New', Courier, monospace;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            border: 1px solid #00ff41;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0, 255, 65, 0.2);
            text-align: center;
            width: 300px;
        }
        h2 { margin-bottom: 20px; }
        input {
            width: 90%;
            padding: 10px;
            margin: 10px 0;
            background: #222;
            border: 1px solid #00ff41;
            color: white;
            border-radius: 5px;
            font-size: 16px;
        }
        button {
            width: 100%;
            padding: 12px;
            background: #00ff41;
            color: black;
            border: none;
            font-weight: bold;
            cursor: pointer;
            border-radius: 5px;
            font-size: 16px;
            margin-top: 10px;
        }
        button:hover { background: #00cc33; }
        #status { margin-top: 20px; font-size: 14px; }
        .loading { color: yellow; }
        .success { color: #00ff41; }
    </style>
</head>
<body>

    <div class="container">
        <h2>SECURE OTP TESTER</h2>
        <p style="font-size: 12px; color: #888;">(Educational UI Demo)</p>
        
        <input type="text" id="mobile" placeholder="Enter Mobile Number" maxlength="10">
        <button onclick="sendOTP()">SEND OTP</button>
        
        <div id="status"></div>
    </div>

    <script>
        function sendOTP() {
            const mobile = document.getElementById('mobile').value;
            const statusDiv = document.getElementById('status');

            if (mobile.length < 10) {
                statusDiv.innerHTML = "<span style='color:red;'>Invalid Number</span>";
                return;
            }

            statusDiv.innerHTML = "<span class='loading'>Processing Request...</span>";

            // Backend ko request bhejna
            fetch('/send-otp', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ number: mobile })
            })
            .then(response => response.json())
            .then(data => {
                statusDiv.innerHTML = "<span class='success'>" + data.message + "</span>";
            })
            .catch(error => {
                statusDiv.innerHTML = "<span style='color:red;'>Error!</span>";
            });
        }
    </script>
</body>
</html>
"""

# ==========================================
# BACKEND LOGIC (Python)
# ==========================================
@app.route('/')
def home():
    # Jab user website kholega, HTML dikhao
    return render_template_string(HTML_CODE)

@app.route('/send-otp', methods=['POST'])
def send_otp():
    data = request.json
    mobile_number = data.get('number')
    
    # ---------------------------------------------------------
    # ---------------------------------------------------------
    
    print(f"Request received for: {mobile_number}")
    time.sleep(2)
    return jsonify({
        "status": "success", 
        "message": f"Verified! Simulation OTP sent to {mobile_number}"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000
import requests
import json

def send_legitimate_otp(mobile_number, api_key):
    # Yeh URL aapke SMS Provider ka hona chahiye (Example:ConfirmTkt, JustDial, Allen Solly, etc.)
    # Note: Public websites (JustDial etc.) ka URL yahan kaam nahi karega.
    url = "https://securedapi.confirmtkt.com/api/platform/register?newOtp=true&mobileNumber={target}"
    
    # Payload aapke provider ke documentation ke hisaab se hoga
    payload = {
        "route": "otp",
        "variables_values": "123456",  # Generated OTP
        "numbers": mobile_number,
    }
    
    headers = {
    "authorization": api_key,  # Yahan code ek chhota token expect kar raha hai
    ...
    }

    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        
        if response.status_code == 200:
            print(f"Success! OTP sent to {mobile_number}")
            print("Response:", response.text)
        else:
            print(f"Failed. Status Code: {response.status_code}")
            print("Error:", response.text)
            
    except Exception as e:
        print(f"Connection Error: {e}")

# Usage
if __name__ == "__main__":
    my_api_key = "1.https://securedapi.confirmtkt.com/api/platform/register?newOtp=true&mobileNumber=
2.https://t.justdial.com/api/india_api_write/18july2018/sendvcode.php?mobile=
3.https://www.allensolly.com/capillarylogin/validateMobileOrEMail
 4.https://www.frotels.com/appsendsms.php 
5. https://www.gapoon.com/userSignup
6. https://login.housing.com/api/v2/send-otp
7. https://porter.in/restservice/send_app_link_sms 
8.https://cityflo.com/website-app-download-link-sms/
9.https://api.nnnow.com/d/api/appDownloadLink 
10.https://login.web.ajio.com/api/auth/signupSendOTP 
11.https://www.happyeasygo.com/heg_api/user/sendRegisterOTP.do?phone=91%20 
12.https://unacademy.com/api/v1/user/get_app_link/
13.https://www.treebo.com/api/v2/auth/login/otp/  
14.https://www.airtel.in/referral-api/core/notify?messageId=map&rtn=
15.https://pharmeasy.in/api/auth/requestOTP 
16.https://www.mylescars.com/usermanagements/chkContact 
17.https://grofers.com/v2/accounts/
18. https://api.dream11.com/sendsmslink 
19.https://www.cashify.in/api/cu01/v1/app-link?mn= 
20.https://commonfront.paytm.com/v4/api/sendsms 
21.https://online.kfc.co.in/OTP/ResendOTPToPhoneForLogin 
22.https://indialends.com/internal/a/mobile-verification_v2.ashx"
    target_number = "9998887776"
    
    send_legitimate_otp(target_number, my_api_key)
