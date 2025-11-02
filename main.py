from weather_api import get_weather
from outfit_logic import ai_outfit_suggestion
from notifier import notify  
from config import TIME, CITY, TELEGRAM_TOKEN
import schedule, time, threading, os
from datetime import datetime
from flask import Flask
import telebot

bot = telebot.TeleBot(TELEGRAM_TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Weather Outfit Notifier is running successfully on Render!"


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
    print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ AI Outfit suggestion sent.")


def run_scheduler():
    print("🕒 Scheduler started...")
    schedule.every().day.at(TIME).do(daily_weather_update)
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    threading.Thread(target=run_scheduler, daemon=True).start()

  
    port = int(os.environ.get("PORT", 10000))
    print(f"🚀 Starting Flask server on port {port}...")
    app.run(host="0.0.0.0", port=port)
