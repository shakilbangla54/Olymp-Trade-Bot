import os
import time
from flask import Flask
from threading import Thread

# Flask ওয়েব সার্ভার (রেন্ডারকে সচল রাখার জন্য)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# আপনার বটের মূল কাজ
def bot_engine():
    print("Bot engine has started successfully!")
    while True:
        print("Monitoring market data... Active status.")
        time.sleep(60) # প্রতি ৬০ সেকেন্ডে লগে একটি মেসেজ দেবে

if __name__ == "__main__":
    # ওয়েব সার্ভার এবং বটের কাজ একসাথে চালু করা
    Thread(target=run_flask).start()
    bot_engine()
