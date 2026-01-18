import requests
import time
import sys
from colorama import Fore, Style, init

# Colors ko initialize karein
init(autoreset=True)

# --- CONFIGURATION ---
# Aapki di gayi API
API_URL = "https://securedapi.confirmtkt.com/api/platform/register?newOtp=true&mobileNumber={}"
DELAY = 15  # Har 15 seconds mein SMS jayega (Jaisa HTML mein tha)

def banner():
    print(Fore.CYAN + """
    ╔════════════════════════════════════╗
    ║      ConfirmTkt OTP Sender         ║
    ║     (Python Fixed Version)         ║
    ╚════════════════════════════════════╝
    """ + Style.RESET_ALL)

def send_otp(mobile, count_display):
    try:
        # URL mein number daalna
        formatted_url = API_URL.format(mobile)
        
        # Headers (Browser ban kar request bhejna)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        
        # Request bhejna (GET request)
        response = requests.get(formatted_url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            print(Fore.GREEN + f"[{count_display}] SMS Sent Successfully! ✅")
            return True
        else:
            print(Fore.RED + f"[{count_display}] Failed (Status: {response.status_code}) ❌")
            return False
            
    except Exception as e:
        print(Fore.RED + f"[{count_display}] Network Error: {e} ❌")
        return False

def main():
    banner()
    
    # Step 1: Input Mobile Number
    mobile = input(Fore.YELLOW + "Enter Mobile Number (10 digits): " + Style.RESET_ALL).strip()
    
    # Basic validation
    if len(mobile) != 10 or not mobile.isdigit():
        print(Fore.RED + "Error: Please enter a valid 10-digit number.")
        return

    print(Fore.CYAN + "\n--- Step 1: Testing Single OTP ---")
    print("Sending 1 OTP to check if API is working...")
    
    # Pehla SMS bhejna check karne ke liye
    if send_otp(mobile, "TEST"):
        print(Fore.GREEN + "\nAPI is Working Perfectly!")
        
        # Step 2: Loop Confirmation
        choice = input(Fore.YELLOW + f"\nStart sending SMS every {DELAY} seconds? (y/n): " + Style.RESET_ALL)
        
        if choice.lower() == 'y':
            print(Fore.CYAN + f"\n--- Step 2: Starting Loop (Ctrl+C to Stop) ---")
            count = 1
            try:
                while True:
                    send_otp(mobile, count)
                    count += 1
                    print(Fore.BLUE + f"Waiting {DELAY} seconds..." + Style.RESET_ALL)
                    time.sleep(DELAY)
            except KeyboardInterrupt:
                print(Fore.RED + "\n\nProcess Stopped by User.")
        else:
            print(Fore.CYAN + "Process Cancelled.")
            
    else:
        print(Fore.RED + "\nAPI check failed. SMS nahi gaya.")

if __name__ == "__main__":
    main()
