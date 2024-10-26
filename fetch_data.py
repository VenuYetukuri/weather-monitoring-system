# fetch_data.py
import requests
from config import API_KEY, BASE_URL, CITIES

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        # Convert temperatures from Kelvin to Celsius
        data['main']['temp'] -= 273.15
        data['main']['feels_like'] -= 273.15
        return {
            "city": city,
            "temp": data['main']['temp'],
            "feels_like": data['main']['feels_like'],
            "weather": data['weather'][0]['main'],
            "timestamp": data['dt']
        }
    else:
        print(f"Failed to fetch data for {city}")
        return None

def fetch_all_cities():
    return [get_weather(city) for city in CITIES]
