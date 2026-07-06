import os
import time
from flask import Flask
from threading import Thread

# Flask সার্ভার সেটআপ
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# বটের কাজ করার জন্য আলাদা ফাংশন
def bot_process():
    print("Bot process started!") # এটি আপনার লগে দেখাবে
    while True:
        print("Monitoring market...") # এটি প্রতি মিনিটে লগে আসবে
        # আপনার ট্রেডিং লজিক বা সিগন্যাল এখানে থাকবে
        time.sleep(60) 

if __name__ == "__main__":
    # Flask কে আলাদা থ্রেডে চালু করা
    Thread(target=run_flask).start()
    # বট প্রসেস চালু করা
    bot_process()
