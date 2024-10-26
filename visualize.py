
import matplotlib.pyplot as plt

def plot_daily_summary(summaries):
    for city, summary in summaries.items():
        dates = summary["date"]
        temps = [summary["average_temp"]]
        
        plt.plot(dates, temps, label=city)
    
    plt.xlabel("Date")
    plt.ylabel("Average Temperature (°C)")
    plt.legend()
    plt.title("Daily Weather Summary")
    plt.show()
