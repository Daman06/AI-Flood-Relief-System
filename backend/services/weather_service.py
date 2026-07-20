import requests


def get_weather(latitude, longitude):

    # Check if coordinates exist
    if latitude is None or longitude is None:
        return {
            "error": True,
            "reason": "Latitude or Longitude is missing."
        }

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current=temperature_2m,precipitation,rain,weather_code"
        "&hourly=rain,precipitation"
        "&past_days=1"
        "&forecast_days=2"
        "&timezone=auto"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        # Open-Meteo returned an error
        if "error" in data:
            return {
                "error": True,
                "reason": data.get("reason", "Weather API Error")
            }

        return data

    except Exception as e:
        return {
            "error": True,
            "reason": str(e)
        }