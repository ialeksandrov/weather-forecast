# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# Get the page with hardcoded location Sofia
PAGE = requests.get("https://weather.com/weather/today/l/ \
                    3cc6a08e912b5b121b32615df8da9c658a6e469de11b2fa805e0fcb14f8b87da")
# Extracting data
soup = BeautifulSoup(PAGE.content, 'html.parser')
location = soup.find('h1', class_="h4 today_nowcard-location").text
temperature = soup.find('div', class_='today_nowcard-temp').text
PHRASE = soup.find('div', class_='today_nowcard-phrase').text
feels_like = soup.find('span', class_='deg-feels').text
table = soup.find('table')
degree_sign = "\u00b0"


def location_formatter(location):
    """
        The role of this function is to fix the location display.
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
    """
       Simple metric convertor from Fahrenheit to Celsius
       This function takes:
       :parameter temperature in Fahrenheit
       :returns temperature in Celsius
    """
    temperature = temperature[:-1]
    temperature = ((float(temperature) - 32) / 1.8)

    return temperature


if PAGE.status_code == 200:
    print("Location:{}".format(location_formatter(location)))
    print("Temperature: {}{} {}".format(round(temperature_convertor(temperature)), degree_sign, PHRASE))
    print("Feels like: {}{}".format(round(temperature_convertor(feels_like)), degree_sign))
    output_rows = []
    for table_row in table.findAll('tr'):
        columns = table_row.findAll('td')
        headers = table_row.findAll('th')
        output_row = []
        for column in columns:
            for header in headers:
                output_row.append(header.text)
            output_row.append(column.text)
        output_rows.append(output_row)
        print(output_row)
else:
    print("ERROR: No weather forecast available!")
