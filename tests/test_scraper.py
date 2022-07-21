import requests


def test_get_request_to_the_weather_site():
    page = requests.get("https://www.yr.no/en/forecast/daily-table/2-727011/Bulgaria/Sofia-Capital/Sofia/Sofia")
    assert page.status_code == 200

