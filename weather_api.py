import requests
from config import API_KEY, CITY

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    data = requests.get(url).json()
    
    temp = data["main"]["temp"]
    condition = data["weather"][0]["main"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    
    return temp, condition, humidity, wind_speed
