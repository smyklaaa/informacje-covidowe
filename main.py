import requests


def make_list_of_countries():
    """tworzenie listy panstw dostepnych w bazie danych"""

    response = requests.get("https://api.covid19api.com/countries")
    data = response.json()
    for country in data:
        print(country)

make_list_of_countries()