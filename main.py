from weather_api import get_weather
from outfit_logic import ai_outfit_suggestion
from notifier import notify  
from config import TIME, CITY
import schedule, time
from datetime import datetime
import telebot
from config import TELEGRAM_TOKEN
from flask import Flask
import threading
from notifier import run_bot
import os

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def daily_weather_update():
    temp, condition, humidity, wind_speed = get_weather()
    outfit = ai_outfit_suggestion(temp, condition, humidity, wind_speed)

    message = (
        f"🌤️ Good morning\n"
        f"📍 Location: {CITY}\n"
        f"🌡️ {temp}°C, {condition}\n"
        f"💧 Humidity: {humidity}% | 🌬️ Wind: {wind_speed} km/h\n\n"
        f"{outfit}"
    )

    notify(message)  
    print(f"[{datetime.now().strftime('%H:%M:%S')}] AI Outfit suggestion sent.")

schedule.every().day.at(TIME).do(daily_weather_update)

print("✅ AI Weather & Outfit Notifier started...")
while True:
    schedule.run_pending()
    time.sleep(60)




app = Flask(__name__)

@app.route('/')
def home():
    return " Weather Outfit Notifier is running!"

def start_bot():
    run_bot()  

if __name__ == "__main__":
    threading.Thread(target=start_bot).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
