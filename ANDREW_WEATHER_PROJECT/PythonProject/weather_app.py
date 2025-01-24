from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv() #it's loading our api key from .env

def get_current_weather(city="Denver"):
    request_url=f"http://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=imperial" #this is our requesting url to the weather website
    weather_data=requests.get(request_url).json() #here we're assigning the "getting url in json data" to weather_data
    return weather_data

if __name__=="__main__":
    print("\nGet Current Weather Conditions")
    city=input(("\nPlease enter a city name: "))
    if not bool(city.strip()): #it means that we're stripping the whitespaces on both sides and checking if it's an empty string. If it's then we're gonna return Denver as default city
        city="Denver"
    weather_data=get_current_weather(city)
    pprint(weather_data)

#this code is for the Python console. This code not depending on the "weather_server.py" file and can be run by itself