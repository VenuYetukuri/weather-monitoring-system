# alert_system.py
from config import TEMP_THRESHOLD, ALERT_CONSECUTIVE_LIMIT

alert_log = {}

def check_alert_conditions(data):
    city = data['city']
    temp = data['temp']
    
    if city not in alert_log:
        alert_log[city] = 0
    
    # Check if temperature exceeds threshold
    if temp > TEMP_THRESHOLD:
        alert_log[city] += 1
    else:
        alert_log[city] = 0  # Reset if threshold not exceeded
    
    # Trigger alert if threshold is breached consecutively
    if alert_log[city] >= ALERT_CONSECUTIVE_LIMIT:
        print(f"ALERT: High temperature in {city} - {temp}°C")
