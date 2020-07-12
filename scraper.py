import requests
from bs4 import BeautifulSoup

# Get the page with hardcoded location Sofia
PAGE = requests.get("https://weather.com/weather/today/l/ \
                    3cc6a08e912b5b121b32615df8da9c658a6e469de11b2fa805e0fcb14f8b87da")
# Extracting data
soup = BeautifulSoup(PAGE.content, 'html.parser')
location = soup.find('h1', class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--location--1YWj_").text
temperature = soup.find('div', class_='_-_-components-src-organism-CurrentConditions-CurrentConditions--primary--2DOqs').text
phrase = soup.find('div', class_='_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf').text
feels_like = soup.find('span', class_='_-_-components-src-organism-TodayDetailsCard-TodayDetailsCard--feelsLikeTempValue--2icPt').text
wind_speed = soup.find('span', class_='_-_-components-src-atom-WeatherData-Wind-Wind--windWrapper--3Ly7c').text


def location_formatter(location):
    """
        The role of this function is to fix the location display.
        - by default the location is displayed in the following way:
          - "Sofia, Sofia, Bulgaria"
        One "Sofia" is not needed, so this function will strip the unneeded "Sofia"

        :returns "Sofia, Bulgaria Weather"
    """
    location = location.split(',')
    location = location[1:]
    location = ",".join(location)

    return location


if __name__ == "__main__":
    if PAGE.status_code == 200:
        print("Location:{}".format(location_formatter(location)))
        print("Temperature: {}".format(temperature))
        print("Feels like: {}".format(feels_like))
        print("Additional info: {}".format(phrase))
        print("Wind: {}".format(wind_speed))
    else:
        print("ERROR: No weather forecast available!")
