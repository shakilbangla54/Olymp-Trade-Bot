import os
import time
import requests
from flask import Flask
from threading import Thread

# আপনার কনফিগারেশন
BOT_TOKEN = "8935684819:AAHUzLPPpVmC10VXUM1SG1esWpFAFE4Taxk"
CHAT_ID = "7627603437"

# টেলিগ্রামে মেসেজ পাঠানোর ফাংশন
def send_telegram_message(signal):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={signal}"
    try:
        requests.get(url)
    except Exception as e:
        print(f"Telegram error: {e}")

# ওয়েব সার্ভার
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is running perfectly!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# ট্রেডিং লজিক (নিখুঁত করার জন্য এখানে আপনার শর্তগুলো বসাব)
def trading_bot_engine():
    print("Engine started: Monitoring...")
    while True:
        # এখানে আমরা ১০০ ক্যান্ডেল এনালাইসিস করে সিগন্যাল ডিটেক্ট করব
        # আপাতত টেস্ট করার জন্য আমরা লুপটি চালু রাখলাম
        
        # উদাহরন: সিগন্যাল পাওয়ার পর এভাবে কল করবেন:
        # send_telegram_message("UP") বা send_telegram_message("DOWN")
        
        time.sleep(60)

if __name__ == "__main__":
    Thread(target=run_flask).start()
    trading_bot_engine()
