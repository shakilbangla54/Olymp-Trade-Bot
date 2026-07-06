import os
import time
import requests
from flask import Flask
from threading import Thread

# আপনার তথ্য
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
    return "Bot is running and monitoring!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def trading_bot_engine():
    print("Engine started: Monitoring market conditions...")
    while True:
        try:
            # এখানে আমরা এনালাইসিস শুরু করব
            print("Status: Analysis cycle running...")
            
            # --- এখানে ভবিষ্যতে EMA/RSI এর শর্ত বসবে ---
            # আপাতত আমরা একটি টেস্ট মেসেজ পাঠাবো কি না চেক করার জন্য
            # send_telegram_message("Bot test signal") 
            
            time.sleep(60) # প্রতি ১ মিনিট পর পর এনালাইসিস করবে
        except Exception as e:
            print(f"Engine Error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    Thread(target=run_flask).start()
    trading_bot_engine()
