import requests
from datetime import datetime
import os
from dotenv import load_dotenv
from flask import Flask, render_template_string

load_dotenv()
# initialize Flask
app = Flask(__name__)


# only using default city when trying to run as cron job
# city = os.getenv("DEFAULT_CITY", "Miami").strip()
API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
FORECAST_URL = os.getenv("FORECAST_URL")
city = os.getenv("DEFAULT_CITY", "London").strip()

# ask for city


def daily_weather(city):
    # set up API key- .env

    # set up current weather API url
    daily_api_url = f"{API_URL}?query={city}&key={API_KEY}&units=imperial"
    try:
        weather = requests.get(daily_api_url)

        if weather.status_code == 200:
            city_weather = weather.json()  # current weather

        # try:
        # Changed indentation to align with try block
            city_name = city_weather["city"]
            temp = round(city_weather["temperature"]["current"])

        # Display current temperature
            return f"<h1>The current temperature for {city_name} is {temp}°F.</h1>"

        else:
            return f"<h3 style='color: red;'>Failed to retrieve data.</h3>"
    except Exception as e:
        return f"<h3 style = 'color: red;'>rror fetching weather: {str(e)}</h3>"


def forecast_weather(city):

    request_forecast_url = f'{FORECAST_URL}forecast?query={city}&key={API_KEY}&units=imperial'
    try:
        forecast = requests.get(request_forecast_url)

        if forecast.status_code != 200:
            return f"<p>Forecast unavailable.</p>"

        city_forecast = forecast.json()
        forecast_output = "<h3>7-Day Forecast</h3><ul>"  # List to collect all days

        for day in city_forecast.get("daily", []):
            timestamp = day['time']  # get timestamp by date
            forecast_dt = datetime.fromtimestamp(
                timestamp)  # convert timestamp to date
            format_date = forecast_dt.date()  # convert timestamp to date
            forecast_date = format_date.strftime(
                "%a")  # timestamp to day of week

            temperature_future = round(day['temperature']['day'])
        # forecasted temp for x days

            if forecast_dt.date() != datetime.today().date():
                # for timestamp in city_forecast:
                forecast_output += f"<li><b>{forecast_date}</b>: {temperature_future}°F</li>"

        forecast_output += "</ul>"
        return forecast_output

    except Exception as e:
        return (
            f"<h3 style='color: red;'>Error fetching forecast: {str(e)}</h3>"
        )


def credit():
    return "<p style= color:'green'; text-align:'centered;'>Created by Amy Rowell</p>"


@app.route("/")
@app.route("/<city>")
def home(city=None):
    # need error checking if no city entered
    if not city:
        city = os.getenv("DEFAULT_CITY", "London").strip()

    if not city:
        return "<h2>Error: Please configure a valid default city name.</h2>"

    current_html = daily_weather(city)
    forecast_html = forecast_weather(city)
    credit_html = credit()

    web_page = f"""
    <html>
        <head>
        <title>Weather App</title>
        <style>
         body {{ background-color: #DBD4ff; 
         color:#723480;
        font-family: Arial, sans-serif; 
        margin: 60px auto;
        padding: 20px;
        border-radius: 12px;
        border-color: #808034;
        border-padding: 20px;
        border-style: solid;
        border-width: 5px;}}
        html {{
             background-color: #FFFFE3; 
                }}
        >
        </style>
        </head>
        <body>
            <h1>🌤️ Weather Forecast for {city.title()}</h1>
            {current_html}
            {forecast_html}
            {credit_html}
        </body>
    
    </html>
    """
    return web_page


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
