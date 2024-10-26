# process_data.py
from datetime import datetime
from collections import defaultdict

# Store data per city in memory for demonstration purposes
daily_data = defaultdict(list)

def process_weather_data(data):
    city = data['city']
    temp = data['temp']
    timestamp = data['timestamp']
    
    date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    
    # Store temperature data for rollup
    daily_data[city].append({
        "date": date,
        "temp": temp,
        "weather": data['weather']
    })

def calculate_daily_summary():
    summaries = {}
    for city, records in daily_data.items():
        date = records[0]['date']
        temps = [record['temp'] for record in records]
        weathers = [record['weather'] for record in records]
        
        average_temp = sum(temps) / len(temps)
        max_temp = max(temps)
        min_temp = min(temps)
        dominant_weather = max(set(weathers), key=weathers.count)
        
        summaries[city] = {
            "date": date,
            "average_temp": average_temp,
            "max_temp": max_temp,
            "min_temp": min_temp,
            "dominant_weather": dominant_weather
        }
    return summaries
