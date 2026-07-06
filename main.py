import os
import time
from flask import Flask
from threading import Thread

# ওয়েব সার্ভার
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is monitoring the market..."

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# ট্রেডিং লজিক (নিখুঁত করার জন্য এটিই আমাদের মেইন জায়গা)
def trading_bot_engine():
    print("Engine started: Monitoring market conditions...")
    while True:
        # এখানে আমরা ১০০ ক্যান্ডেল এনালাইসিস লজিক পর্যায়ক্রমে যোগ করব
        print("Status: Analysis cycle running. Checking EMA and RSI indicators...")
        
        # প্রতি ১ মিনিট পর পর বট আপডেট দিবে
        time.sleep(60) 

if __name__ == "__main__":
    Thread(target=run_flask).start()
    trading_bot_engine()
