import asyncio
from telegram import Bot
from config import TELEGRAM_TOKEN, CHAT_ID

async def send_notification(message: str):
    bot = Bot(token=TELEGRAM_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message)

def notify(message: str):
    asyncio.run(send_notification(message))
