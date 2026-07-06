import os
import sys
import time
import requests
import pandas as pd
import pandas_ta as ta
import yfinance as yf
from flask import Flask
from threading import Thread

# বাফার ঠিক রাখা যাতে লগে সব মেসেজ সাথে সাথে দেখা যায়
sys.stdout.reconfigure(line_buffering=True)

# আপনার কনফিগারেশন
BOT_TOKEN = "8935684819:AAHUzLPPpVmC10VXUM1SG1esWpFAFE4Taxk"
CHAT_ID = "7627603437"
SYMBOL = "EURUSD=X"

app = Flask(__name__)

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    try:
        requests.get(url)
    except Exception as e:
        print(f"Telegram error: {e}")

@app.route('/')
def home():
    return "Bot is running and monitoring market!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def trading_logic():
    print("LOG: Trading logic engine started...", flush=True)
    while True:
        try:
            # লাইভ ডেটা সংগ্রহ
            df = yf.download(SYMBOL, period="1d", interval="1m", progress=False)
            
            if not df.empty:
                # ইন্ডিকেটর গণনা
                df['RSI'] = ta.rsi(df['Close'], length=14)
                df['EMA'] = ta.ema(df['Close'], length=50)
                
                last_rsi = df['RSI'].iloc[-1]
                last_price = df['Close'].iloc[-1]
                last_ema = df['EMA'].iloc[-1]

                # সিগন্যাল কন্ডিশন
                if last_rsi < 30 and last_price > last_ema:
                    send_telegram("🚀 সিগন্যাল: UP (Buy)")
                elif last_rsi > 70 and last_price < last_ema:
                    send_telegram("📉 সিগন্যাল: DOWN (Sell)")
                
                print(f"LOG: Market checked. Price: {last_price:.4f}, RSI: {last_rsi:.2f}", flush=True)
            
        except Exception as e:
            print(f"LOG: Error in logic: {e}", flush=True)
            
        time.sleep(60) # প্রতি ১ মিনিট পর পর চেক করবে

if __name__ == "__main__":
    Thread(target=run_flask).start()
    trading_logic()
