# main.py
import time
from fetch_data import fetch_all_cities
from process_data import process_weather_data, calculate_daily_summary
from alert_system import check_alert_conditions
from visualize import plot_daily_summary
from config import FETCH_INTERVAL

def main():
    while True:
        weather_data = fetch_all_cities()
        for data in weather_data:
            if data:
                process_weather_data(data)
                check_alert_conditions(data)
        
        # Calculate and display daily summaries at the end of each day
        if datetime.now().hour == 23 and datetime.now().minute == 59:  # end of day
            summaries = calculate_daily_summary()
            plot_daily_summary(summaries)
        
        time.sleep(FETCH_INTERVAL)

if __name__ == "__main__":
    main()
