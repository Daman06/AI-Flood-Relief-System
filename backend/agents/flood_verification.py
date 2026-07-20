import json

from models.state import RescueState
from services.weather_service import get_weather
from tools.llm import llm


def flood_verification_agent(state: RescueState) -> RescueState:

    print("Flood Verification Agent Started")

    latitude = state["latitude"]
    longitude = state["longitude"]

    print(f"User Coordinates: {latitude}, {longitude}")

    # Fetch live weather
    weather = get_weather(latitude, longitude)

    print("===== WEATHER CHECK =====")
    print(weather)
    print("=========================")

    # Weather API failed
    if weather.get("error"):
        print("Weather API failed:", weather.get("reason"))

        state["flood_verified"] = False
        state["risk_level"] = "Unknown"
        state["verification_reason"] = weather.get(
            "reason", "Weather API unavailable."
        )

        return state

    current = weather.get("current", {})
    hourly = weather.get("hourly", [])

    # Calculate rainfall
    try:
        past_24h_rain = sum(hourly["rain"][:24])
        next_24h_rain = sum(hourly["rain"][24:48])
    except Exception:
        try:
            past_24h_rain = sum(h.get("rain", 0) for h in hourly[:24])
            next_24h_rain = sum(h.get("rain", 0) for h in hourly[24:48])
        except Exception:
            past_24h_rain = 0
            next_24h_rain = 0

    print(f"Past 24h Rain: {past_24h_rain}")
    print(f"Next 24h Rain: {next_24h_rain}")

    prompt = f"""
You are an expert flood verification AI.

Current Weather

Temperature: {current.get('temperature_2m', 'N/A')} °C
Current Rain: {current.get('rain', 'N/A')} mm
Current Precipitation: {current.get('precipitation', 'N/A')} mm
Weather Code: {current.get('weather_code', 'N/A')}

Recent Weather

Rain in last 24 hours: {past_24h_rain} mm

Forecast

Expected rain in next 24 hours: {next_24h_rain} mm

Victim Message:
{state.get("emergency_message", "")}

Important:
- Do NOT reject a rescue request only because it is not raining now.
- Flooding can continue after earlier heavy rainfall, river overflow, dam releases, or poor drainage.
- Treat the victim's report as important evidence.
- Use both weather data and the victim's description.

Respond ONLY in JSON:

{{
    "flood_verified": true,
    "risk_level": "High",
    "reason": "Short explanation"
}}
"""

    response = llm.invoke(prompt)

    print("===== FLOOD AI RESPONSE =====")
    print(response.content)
    print("=============================")

    try:
        content = response.content.strip()

        if content.startswith("```"):
            content = content.replace("```json", "")
            content = content.replace("```", "")
            content = content.strip()

        result = json.loads(content)

        state["flood_verified"] = result.get("flood_verified", False)
        state["risk_level"] = result.get("risk_level", "Unknown")
        state["verification_reason"] = result.get(
            "reason", "No reason provided"
        )

    except Exception as e:
        print("JSON Parsing Error:", e)

        state["flood_verified"] = False
        state["risk_level"] = "Unknown"
        state["verification_reason"] = "Unable to parse AI response."

    return state