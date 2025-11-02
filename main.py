from weather_api import get_weather
from outfit_logic import ai_outfit_suggestion
from notifier import notify  # use the sync wrapper
from config import TIME, CITY
import schedule, time
from datetime import datetime
import telebot
from config import TELEGRAM_TOKEN

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def daily_weather_update():
    temp, condition, humidity, wind_speed = get_weather()
    outfit = ai_outfit_suggestion(temp, condition, humidity, wind_speed)

    message = (
        f"🌤️ Good morning, Sam!\n"
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
