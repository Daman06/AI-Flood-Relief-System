import json

from services.weather_service import get_weather
from tools.llm import llm


def flood_alert_agent(latitude, longitude):

    weather = get_weather(latitude, longitude)

    if weather.get("error"):
        return weather

    current = weather.get("current", {})
    hourly = weather.get("hourly", {})

    past_24h_rain = sum(hourly.get("rain", [])[:24])
    next_24h_rain = sum(hourly.get("rain", [])[24:48])

    prompt = f"""
You are an expert flood early warning AI.

Current Weather

Temperature: {current.get("temperature_2m")}
Current Rain: {current.get("rain")}
Current Precipitation: {current.get("precipitation")}
Weather Code: {current.get("weather_code")}

Recent Rainfall:
{past_24h_rain} mm

Forecast Rainfall (Next 24 Hours):
{next_24h_rain} mm

Your job is to decide if an EARLY FLOOD ALERT should be issued.

Consider:

- Recent rainfall
- Forecast rainfall
- Flood possibility
- Continued rainfall
- Weather severity

Return ONLY JSON.

{{
"alert": true,
"risk": "High",
"message": "Heavy rainfall is expected. Move to safer locations and stay alert."
}}
"""

    response = llm.invoke(prompt)

    try:
        content = response.content.replace("```json", "").replace("```", "").strip()

        return json.loads(content)

    except Exception:

        return {
            "alert": False,
            "risk": "Unknown",
            "message": "Unable to generate flood alert."
        }