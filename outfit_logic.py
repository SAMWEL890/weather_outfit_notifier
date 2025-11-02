# ===============================================================
#  ai_outfit_logic.py | Hybrid AI Outfit Suggestion System 🤖🧥
# ===============================================================
#  Uses OpenAI for intelligent outfit advice, but automatically
#  falls back to a local logic system if the AI is unavailable.
# ===============================================================

import random
from openai import OpenAI
from config import OPENAI_API_KEY

# --- Fallback logic (local suggestion if AI fails) ---
def local_outfit_suggestion(temp, condition, humidity=None, wind_speed=None):
    """Offline fallback outfit suggestion."""
    condition = condition.lower()
    vibe = random.choice(["🌤️", "☁️", "🌧️", "🥶", "🔥", "😎"])

    if temp < 15:
        outfit = "Heavy jacket, warm hoodie, and boots."
    elif 15 <= temp < 22:
        outfit = "A cozy hoodie or light sweater with jeans."
    elif 22 <= temp < 28:
        outfit = "T-shirt and jeans — perfect weather vibes."
    else:
        outfit = "Light shirt, shorts, and a cap — it’s hot out!"

    if "rain" in condition:
        outfit = "Carry an umbrella ☔ and wear waterproof shoes."
    elif "wind" in condition or (wind_speed and wind_speed > 20):
        outfit += " It’s windy — keep a jacket handy 🧥."
    elif "clear" in condition or "sun" in condition:
        outfit += " Don’t forget your sunglasses 😎."

    endings = [
        "Stay comfy and stylish today!",
        "Weather can be sneaky — dress smart 😉",
        "Confidence is the best outfit, rock it! 💪",
        "You got this day, stay fresh ✨",
    ]
    return f"{vibe} {outfit}\n💡 Tip: {random.choice(endings)}"


# --- AI-powered suggestion ---
def ai_outfit_suggestion(temp, condition, humidity=None, wind_speed=None):
    """Ask OpenAI to generate a dynamic outfit suggestion."""
    client = OpenAI(api_key=OPENAI_API_KEY)
    prompt = f"""
    You are a fun, friendly fashion assistant that helps users decide what to wear.
    Here’s today’s weather:
    - Temperature: {temp}°C
    - Condition: {condition}
    - Humidity: {humidity if humidity else 'unknown'}%
    - Wind speed: {wind_speed if wind_speed else 'unknown'} km/h

    Suggest an outfit in a short, casual, and human way (2 sentences max).
    Include emojis and personality — but don't sound robotic.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=60,
        )
        ai_text = response.choices[0].message.content.strip()
        return f"🤖 {ai_text}"

    except Exception as e:
        print(f"⚠️ AI failed: {e}")
        print("🧥 Switching to local outfit logic...")
        return local_outfit_suggestion(temp, condition, humidity, wind_speed)
