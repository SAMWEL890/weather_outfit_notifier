from dotenv import load_dotenv
import os

load_dotenv()

CITY = os.getenv("CITY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
API_KEY = os.getenv("WEATHER_API_KEY")
TIME = os.getenv("TIME", "15:34") 
