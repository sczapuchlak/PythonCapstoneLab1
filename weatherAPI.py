# Python import statements.... https://grahamwideman.wikispaces.com/Python-+import+statement
import urllib.request as request
from urllib.parse import quote
import json


# Fetches weather from openweatherapi, extracts temp from json

# API documentation at http://openweathermap.org/api

# urllib documentation at https://docs.python.org/3.5/library/urllib.parse.html?highlight=urlparse#urllib.parse.urlparse


def get_temp(city, country):
    key = '61b59af80f42ac0c3e27dd243c319cdb'  # TODO sign up for your own account and replace this with your own key!

    # Characters such as spaces, apostrophes, quotes... are not permitted in URLs.
    # The quote function encodes prohibited characters so they can be used in a URL.

    weatherurl = 'http://api.openweathermap.org/data/2.5/weather?q=%s,%s&APPID=%s' \
                 % (quote(city), quote(country), key)

    # For debugging - what URL is being requested?
    print(weatherurl)

    # Add error handling for making the request, and then, for processing the response.
    # Reference: https://docs.python.org/3/tutorial/errors.html

    try:
        # Make request, get response
        weatherResponse = request.urlopen(weatherurl)
    except Exception as e:
        print("Error making request", e)
        return

    # Now try to process the data returned. Again, use exception handling.

    try:

        # Read response into JSON string
        # Reference http://stackoverflow.com/questions/23049767/parsing-http-response-in-python
        wresponseJson = weatherResponse.read().decode('utf-8')

        # For debugging - this displays the full text of the response
        print(wresponseJson)

        # Load JSON string into JSON parser - now can be used in a dictionary-like way
        # Reference http://docs.python-guide.org/en/latest/scenarios/json/
        parsed_json = json.loads(wresponseJson)

        # What's the temp in this city? Extract this particular piece of data from the JSON
        tempInKelvin = parsed_json['main']['temp']

    except Exception as e:
        print('Error processing response', e)
        return

    # OpenWeatherMap returns temperatures in units called Kelvin; to convert Kelvin to Celsius subtract 273
    tempInCelcius = int(tempInKelvin) - 273

    return tempInCelcius


def main():
    city = input("Enter the city to search for")
    country = input("What country is that in?")
    temp = get_temp(city, country)
    if temp is not None:
        print('The temperature in %s %s is %f degrees C ' % (city, country, temp))
    else:
        print('Unable to get the temperature.')


main()
