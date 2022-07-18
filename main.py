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
                      "(1)Zakażenia\n(2)Zgony\n(3)Ozdrowieńcy\n")

    while what_next in ("1","2","3"):

        if what_next == "1":
            os.system("cls")
            what_time = input("Wpisz numer danch okresu który chcesz sprawdzić:\n"
                              "(1)Suma w ciagu roku\n(2)Suma w ciągu miesiaca\n"
                              "(3)Suma w ciągu dnia\n(4)Cały okres pandemi\n")
            period_of_time(what_time)

        elif what_next == "2":
            os.system("cls")
            what_time = input("Wpisz numer danch które chcesz sprawdzić:\n"
                              "(1)Suma w ciagu roku\n(2)Suma w ciągu miesiaca\n"
                              "(3)Suma w ciągu dnia\n(4)Cały okres pandemi\n")
            period_of_time(what_time)

        elif what_next == "3":
            os.system("cls")
            what_time = input("Wpisz numer danch które chcesz sprawdzić:\n"
                              "(1)Suma w ciagu roku\n(2)Suma w ciągu miesiaca\n"
                              "(3)Suma w ciągu dnia\n(4)Cały okres pandemi\n")
            period_of_time(what_time)



def make_list_of_countries():
    """tworzenie listy panstw dostepnych w bazie danych"""

    response = requests.get("https://api.covid19api.com/countries")
    data = response.json()
    list_of_countries = []
    for country in data:
        list_of_countries.append(country["Country"])
    return list_of_countries

def period_of_time(what_time, which_data):
    while what_time in ("1", "2", "3", "4"):
        if what_time == "1":
            os.system("cls")


        elif what_time == "2":
            os.system("cls")


        elif what_time == "3":
            os.system("cls")


        elif what_time == "4":
            os.system("cls")



main()