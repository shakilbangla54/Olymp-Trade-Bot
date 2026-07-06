import os
import time
import requests
import pandas as pd
import numpy as np
from flask import Flask
from threading import Thread

# আপনার কনফিগারেশন
BOT_TOKEN = "8935684819:AAHUzLPPpVmC10VXUM1SG1esWpFAFE4Taxk"
CHAT_ID = "7627603437"

def send_telegram_message(signal):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={signal}"
    try:
        requests.get(url)
    except Exception as e:
        print(f"Telegram error: {e}")

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is active and analyzing market!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def trading_bot_engine():
    print("Engine started: Monitoring market...")
    while True:
        try:
            # এখানে আমরা লাইভ মার্কেট ডেটা ফেচ করব (পরবর্তী ধাপে)
            print("Status: Analysis cycle running...")
            
            # ক্যালকুলেশন লজিক এখানে যুক্ত হবে
            # সিগন্যাল পেলে: send_telegram_message("UP") বা "DOWN"
            
            time.sleep(60) # প্রতি মিনিটে এনালাইসিস
        except Exception as e:
            print(f"Engine Error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    Thread(target=run_flask).start()
    trading_bot_engine()
