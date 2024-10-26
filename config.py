# config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
FETCH_INTERVAL = 300  # Interval in seconds
TEMP_THRESHOLD = 35  # Alert threshold in Celsius
ALERT_CONSECUTIVE_LIMIT = 2  # Consecutive threshold breach for alert
