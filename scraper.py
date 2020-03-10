# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# Get the page with hardcoded location Sofia
page = requests.get("https://weather.com/weather/today/l/ \
                    3cc6a08e912b5b121b32615df8da9c658a6e469de11b2fa805e0fcb14f8b87da")
# Extracting data
soup = BeautifulSoup(page.content, 'html.parser')
location = soup.find('h1', class_="h4 today_nowcard-location").text
temperature = soup.find('div', class_='today_nowcard-temp').text
phrase = soup.find('div', class_='today_nowcard-phrase').text
feels_like = soup.find('span', class_='deg-feels').text
degree_sign = "\u00b0"


def location_formatter(location):
    """ The role of this function is to fix the location display.
        - by default the location is displayed in the following way:
          - "Sofia, Sofia, Bulgaria"
        One "Sofia" is not needed, so this function will strip the unneeded "Sofia"

        :returns "Sofia, Bulgaria"
    """
    location = location.split(',')
    location = location[1:]
    location = ",".join(location)

    return location

def temperature_convertor(temperature):
    """Simple metric convertor from Fahrenheit to Celsius
       This function takes:
       :parameter temperature in Fahrenheit
       :returns temperature in Celsius
    """
    temperature = temperature[:-1]
    temperature = ((float(temperature) - 32) / 1.8)

    return temperature


if page.status_code == 200:
    print("Location:{}".format(location_formatter(location)))
    print("Temperature: {}{} {}".format(round(temperature_convertor(temperature)), degree_sign, phrase))
    if round(temperature_convertor(temperature)) < 0:
        print("Temperature: {}{} {}".format(round(temperature_convertor(temperature)), degree_sign, phrase))

    if round(temperature_convertor(feels_like)) < 0:
        print("Feels like: {}{}".format(round(temperature_convertor(feels_like)), degree_sign))
else:
    print("Something went wrong! No weather forecast available!")
