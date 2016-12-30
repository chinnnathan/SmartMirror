__version__ = "0.0.1"
__author__ = "Nathan Chinn"
APIKEY = "673daed241cc2bb6914f191334e0f773"

"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
import pyowm
import json
from SMRT import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    location = "Castle Rock, US"
    weather = get_weather(location)
    message = "Please say \"Smart Mirror help\" for more options"
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        location = location,
        weather = weather,
        message = message,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


def get_weather(location):
    """Returns info about the weather"""
    degree = u"\N{DEGREE SIGN}"
    owm = pyowm.OWM(APIKEY)

    obs = owm.weather_at_place(location)
    w = obs.get_weather()
    windy = w.get_wind()
    temp = w.get_temperature('celsius')

    return( str(temp.get("temp")) + degree + "C wind speed: " + str(windy.get("speed")) )