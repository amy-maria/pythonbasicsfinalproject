import requests
from datetime import datetime
from rich import print
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
FORECAST_URL = os.getenv("FORECAST_URL")
# ask for city
print("[purple bold]Weather Forecast[/purple bold]")
city = input("\nEnter city name: ")
city = city.strip()

# need error checking if no city entered
if city:
    city
else:
    print("Please enter a valid city name.")


def daily_weather(city):
    # set up API key- .env

    # set up current weather API url
    daily_api_url = f"{API_URL}?query={city}&key={API_KEY}&units=imperial"
    weather = requests.get(daily_api_url)

    if weather.status_code == 200:
        city_weather = weather.json()  # current weather

        try:
            # Changed indentation to align with try block
            city_name = city_weather["city"]
            temp = round(city_weather["temperature"]["current"])

            # Display current temperature
            print(f"\nThe current temperature for {city_name} is {temp}°F.\n")

        except KeyError:
            print("Invalid city name. Please try again.")
    else:
        print("Failed to retrieve data.")


def forecast_weather(city):

    request_forecast_url = f'{FORECAST_URL}forecast?query={city}&key={API_KEY}&units=imperial'
    forecast = requests.get(request_forecast_url)

    city_forecast = forecast.json()  # forecast weather

    for day in city_forecast["daily"]:
        timestamp = day['time']  # get timestamp by date
        forecast_dt = datetime.fromtimestamp(
            timestamp)  # convert timestamp to date
        format_date = forecast_dt.date()  # convert timestamp to date
        forecast_date = format_date.strftime("%a")  # timestamp to day of week

        temperature_future = day['temperature']['day']
        # forecasted temp for x days

        if forecast_dt.date() != datetime.today().date():
            # for timestamp in city_forecast:
            print(
                f"[blue]{forecast_date}[/blue]: {round(temperature_future)}°F")


def credit():
    print("\n[green]Created by Amy Rowell[/green]")


daily_weather(city)
forecast_weather(city)
credit()
