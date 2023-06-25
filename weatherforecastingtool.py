import sys
import requests
import json
from datetime import datetime
def get_weather_forecast(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = json.loads(response.text)
    if data["cod"] == "404":
        print("City not found!")
        return
    weather_description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%H:%M:%S')
    sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%H:%M:%S')
    if "rain" in data:
        rain_volume = data["rain"].get("1h", 0)
        print(f"Rain Volume (last 1 hour): {rain_volume} mm")
    if "snow" in data:
        snow_volume = data["snow"].get("1h", 0)
        print(f"Snow Volume (last 1 hour): {snow_volume} mm")
    if "clouds" in data:
        cloudiness = data["clouds"]["all"]
        print(f"Cloudiness: {cloudiness}%")
    if "main" in data:
        pressure = data["main"].get("pressure", 0)
        print(f"Pressure: {pressure} hPa")
    print(f"Weather forecast for {city}:")
    print(f"Description: {weather_description}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Sunrise: {sunrise}")
    print(f"Sunset: {sunset}")
    if temperature >= 25 and temperature <= 35 and humidity >= 50 and humidity <= 80:
        print("Suggested crops: Rice, Wheat, Corn, Cotton")
    elif temperature >= 20 and temperature <= 30 and humidity >= 60 and humidity <= 80:
        print("Suggested crops: Tomato, Potato, Pepper, Pumpkin")
    elif temperature >= 15 and temperature <= 25 and humidity >= 40 and humidity <= 70:
        print("Suggested crops: Lettuce, Spinach, Carrot, Cabbage")
    else:
        print("No specific crop suggestions for this weather")

if __name__ == "__main__":
    api_key = "66fcb85adbdb2f8128f621e46ec3f22e"
    if len(sys.argv) < 2:
        print("Please provide a city name as a command-line argument.")
        sys.exit(1)
    city = sys.argv[1]
    get_weather_forecast(api_key, city)
