from flask import Flask, render_template, request
from weather_app import get_current_weather
from waitress import serve

app=Flask(__name__) #file name represents the module name which corresponds with the python file name where it's running

@app.route("/") #the use of "route" is to define the url path
@app.route("/index") #I WAS TRYING to find out why we're using this url if we can't access it, but I wasn't able to find out. And I have no idea why removing it and the "index" func causing Internal Server Error if there's no such url route on our site at all
def index():
    return render_template("index.html")

@app.route("/weather")
def get_weather():
    city=request.args.get("city") #it means the city that we're about to pass
    if not bool(city.strip()): #it means that we're stripping the whitespaces on both sides and checking if it's an empty string. If it's then we're gonna return Denver as default city
        city="Denver"
    weather_data=get_current_weather(city) #we're assigning the "get_current_weather(city)" func from the "weather_app.py" to the "weather_data" variable
    if not weather_data["cod"]==200:
        return render_template("city-not-found.html") #it means if the city not found then we're rendering this template which tells us to try again
    return render_template( #we're passing title, status, temp and feels_like from the "openweather" site to the "weather.html" template which displays it on our own weather website
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )

if __name__=="__main__":
    serve(app, host="0.0.0.0", port=8000) #it means that we're launching our server on localhost

#this code is for our website. It depends on the "weather_app.py" file because it's using the "get_current_weather" func