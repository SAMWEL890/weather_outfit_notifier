import telebot
from config import TELEGRAM_TOKEN, CHAT_ID

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def notify(message: str):
    try:
        bot.send_message(chat_id=CHAT_ID, text=message)
        print("✅ Message sent successfully.")
    except Exception as e:
        print(f"⚠️ Failed to send message: {e}")
