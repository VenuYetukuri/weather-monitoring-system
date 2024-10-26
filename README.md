Real-Time Weather Monitoring System
This project is a Real-Time Weather Monitoring System designed to retrieve, process, and analyze weather data for major Indian metro cities using the OpenWeatherMap API. It fetches real-time weather data, processes it into daily summaries, triggers alerts based on configurable thresholds, and visualizes weather trends.
Features
Real-Time Data Retrieval: Fetches data at configurable intervals (default is every 5 minutes) from the OpenWeatherMap API.
Data Processing and Aggregation:
Converts temperature to Celsius (or user-preferred units).
Aggregates daily summaries: average, max, and min temperatures, with dominant weather conditions.
Alert System: Configurable temperature and condition-based alerts with console display or optional email notifications.
Visualization: Displays daily summaries and trends.
Technologies Used
Python 3.9+
Docker & Docker Compose (for containerization)
PostgreSQL (database for storing weather data)
Flask (optional for web interface)
Matplotlib/Plotly (for visualization)
Installation and Setup
Prerequisites
Python 3.9 or higher
Docker & Docker Compose
Git (for version control)
1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/weather-monitoring-system.git
cd weather-monitoring-system
2. Install Dependencies
Using Docker Compose (Recommended):

bash
Copy code
docker-compose build
docker-compose up -d
Without Docker:

bash
Copy code
pip install -r requirements.txt
3. Set Up Environment Variables
Create a .env file in the root directory with the following contents:

plaintext
Copy code
OPENWEATHERMAP_API_KEY=your_api_key_here
Additional parameters can be configured in config.py or .env.

4. Run the Application
bash
Copy code
# With Docker Compose
docker-compose up

# Without Docker
python main.py
Configuration
OpenWeatherMap API Key: Sign up at OpenWeatherMap for an API key.
Interval Configuration: Set data-fetch interval in config.py or .env.
Alert Thresholds: Configure temperature and condition thresholds in config.py.
Usage
Data Fetching and Aggregation: Weather data is fetched at specified intervals and processed into daily summaries.
Alert Monitoring: Alerts trigger when configured thresholds are met.
Visualization: View summaries and trends on the console or web interface (if enabled).
Testing
Test Cases
System Setup: Verify API connection.
Data Retrieval: Simulate API calls and validate response parsing.
Temperature Conversion: Validate Kelvin-to-Celsius conversion.
Daily Summary Calculation: Simulate data updates and verify summaries.
Alert System: Configure thresholds and validate alert functionality.
Running Tests
Run test cases using pytest:

bash
Copy code
pytest tests/
Deployment
Docker (Recommended)
Build the Docker Image:

bash
Copy code
docker-compose build
Run the Containers:

bash
Copy code
docker-compose up -d
Check Logs:

bash
Copy code
docker-compose logs -f weather_app
