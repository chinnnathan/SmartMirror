__version__ = "0.0.1"
__author__ = "Nathan Chinn"

"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
import requests
import json
from SMRT import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    weather = get_weather()
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        weather = weather,
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


def get_weather():
    """Returns info about the weather"""
    units = "F"
    loc = "London"
    APIKEY = "10612e11aa4786db990fde1fc9c283ad"
    try:
        u = "http://api.openweathermap.org/data/2.5/weather?q={0}&units={1}"
        u = "api.openweathermap.org/data/2.5/weather?q=London&APPID=" + APIKEY
        r = requests.get(u)
        # r = requests.get(u.format(loc, units))
        j = json.loads(r.text)
    except:
        print("Fuck You")
        return "Cannot Get Weather"

    temp = j['main']['temp']
    temp_unit = 'F' 
    conditions = j['weather'][0]['description']

    return ( conditions, " with temperature of ", temp, u"\u00b0", " ", temp_unit)