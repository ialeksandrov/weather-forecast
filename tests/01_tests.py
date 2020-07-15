import unittest
import requests

from bs4 import BeautifulSoup
from scraper import location_formatter


class TestScraper(unittest.TestCase):

    def test_get_request_to_the_weather_site(self):
        page = requests.get("https://weather.com/weather/today/l/ \
                                            3cc6a08e912b5b121b32615df8da9c658a6e469de11b2fa805e0fcb14f8b87da")
        self.assertEqual(page.status_code, 200)

    def test_location_formatter(self):
        page = requests.get("https://weather.com/weather/today/l/ \
                                            3cc6a08e912b5b121b32615df8da9c658a6e469de11b2fa805e0fcb14f8b87da")
        soup = BeautifulSoup(page.content, 'html.parser')
        location = soup.find('h1', class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--location--1YWj_").text

        self.assertEqual(location_formatter(location), "Sofia,  Bulgaria Weather")


if __name__ == '__main__':
    unittest.main()
