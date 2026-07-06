import os
import sys
import time
from flask import Flask
from threading import Thread

# বাফার বন্ধ করার জন্য যাতে সব লেখা লগে সাথে সাথে দেখায়
sys.stdout.reconfigure(line_buffering=True)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def bot_engine():
    print("LOG: Bot process started successfully!", flush=True)
    while True:
        print("LOG: Monitoring market status...", flush=True)
        time.sleep(60)

if __name__ == "__main__":
    Thread(target=run_flask).start()
    bot_engine()
