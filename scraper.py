import requests
from bs4 import BeautifulSoup

# Get the page with hardcoded location Sofia
PAGE = requests.get("https://www.yr.no/en/forecast/daily-table/2-727011/Bulgaria/Sofia-Capital/Sofia/Sofia")
# Extracting data
soup = BeautifulSoup(PAGE.content, 'html.parser')
location = soup.find('span', class_='page-header__location-name').text
temperature = soup.find('div', class_='now-hero__next-hour-temperature-text').text
feels_like = soup.find('div', class_='feels-like-text').text
wind_speed = soup.find('span', class_='wind__container').text


def location_formatter(location):
    """
        The role of this function is to fix the location display.
        - by default the location is displayed in the following way:
          - "Sofia, Sofia, Bulgaria"
        One "Sofia" is not needed, so this function will strip the unneeded "Sofia"

        :returns "Sofia, Bulgaria Weather"
    """
    location = location.split(',')
    location = location[0:]
    location = ",".join(location)
    location = location.replace("Sia,", "")

    return location


if __name__ == "__main__":
    if PAGE.status_code == 200:
        print("Location{}".format(location_formatter(location)))
        print("Temperature {}".format(temperature))
        print(feels_like)
        print("Wind: {}".format(wind_speed))
    else:
        print("ERROR: No weather forecast available!")
