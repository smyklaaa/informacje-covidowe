import requests
import os


API_URL_COUNTRY = "https://api.covid19api.com/dayone/country/"

def main():
    country = input("Jakie panstwo chcesz sprawdzić? ANG: ")
    while country not in make_list_of_countries():
        country = input("Nie znaleziono kraju, jakie panstwo chcesz sprawdzić? ANG: ")
    response = requests.get(f"{API_URL_COUNTRY}{country}")
    data = response.json()

    what_next = input("Wpisz numer danch które chcesz sprawdzić:\n"
                      "(1)Ile zakażen\n(2)Ile osób zmarło\n(3)Ile ozdrowieńców\n")

    while what_next in ("1","2","3"):

        if what_next == "1":
            os.system("cls")
            what_next = input("Wpisz numer danch okresu który chcesz sprawdzić:\n"
                              "(1)Rok\n(2)Miesiac\n(3)Dzien\n(4)Cały okres pandemi\n")

        elif what_next == "2":
            os.system("cls")
            what_next = input("Wpisz numer danch które chcesz sprawdzić:\n"
                              "(1)Rok\n(2)Miesiac\n(3)Dzien\n(4)Cały okres pandemi\n")

        elif what_next == "3":
            os.system("cls")
            what_next = input("Wpisz numer danch które chcesz sprawdzić:\n"
                              "(1)Rok\n(2)Miesiac\n(3)Dzien\n(4)Cały okres pandemi\n")


def make_list_of_countries():
    """tworzenie listy panstw dostepnych w bazie danych"""

    response = requests.get("https://api.covid19api.com/countries")
    data = response.json()
    list_of_countries = []
    for country in data:
        list_of_countries.append(country["Country"])
    return list_of_countries



main()