import requests
import os
import datetime


API_URL_COUNTRY = "https://api.covid19api.com/dayone/country/"

def main():
    country = input("Jakie panstwo chcesz sprawdzić? ANG: ")
    while country not in make_list_of_countries():
        country = input("Nie znaleziono kraju, jakie panstwo chcesz sprawdzić? ANG: ")
    response = requests.get(f"{API_URL_COUNTRY}{country}")
    main_data = response.json()

    what_next = input("Wpisz numer danych które chcesz sprawdzić:\n"
                      "(1)Zakażenia\n(2)Zgony\n(3)Ozdrowieńcy\n")

    while what_next in ("1","2","3"):

        if what_next == "1":
            os.system("cls")
            what_time = input("Wpisz numer danych okresu który chcesz sprawdzić:\n"
                              "(1)Suma w ciagu roku\n(2)Suma w ciągu miesiaca\n"
                              "(3)Suma w ciągu dnia\n(4)Cały okres pandemi\n")
            what_next = "Confirmed"
            period_of_time(what_time, what_next, main_data)

        elif what_next == "2":
            os.system("cls")
            what_time = input("Wpisz numer danych które chcesz sprawdzić:\n"
                              "(1)Suma w ciagu roku\n(2)Suma w ciągu miesiaca\n"
                              "(3)Suma w ciągu dnia\n(4)Cały okres pandemi\n")
            what_next = "Deaths"
            period_of_time(what_time, what_next, main_data)

        elif what_next == "3":
            os.system("cls")
            what_time = input("Wpisz numer danych które chcesz sprawdzić:\n"
                              "(1)Suma w ciagu roku\n(2)Suma w ciągu miesiaca\n"
                              "(3)Suma w ciągu dnia\n(4)Cały okres pandemi\n")
            what_next = "Recovered"
            period_of_time(what_time, what_next, main_data)



def make_list_of_countries():
    """tworzenie listy panstw dostepnych w bazie danych"""

    response = requests.get("https://api.covid19api.com/countries")
    data = response.json()
    list_of_countries = []
    for country in data:
        list_of_countries.append(country["Country"])
    return list_of_countries

def period_of_time(what_time, which_data, main_data):
    while what_time in ("1", "2", "3", "4"):
        if what_time == "1":
            os.system("cls")
            year = input("Podaj rok ktory chcesz sprawdzić : ")
            first_day_year = f"{year}-01-01"
            first_day_next_year = f"{int(year)+1}-01-01"
            beginning_of_year = search_date(first_day_year, main_data)
            beginning_of_next_year = search_date(first_day_next_year,main_data)
            beginning_of_year = beginning_of_year[which_data]
            beginning_of_next_year = beginning_of_next_year[which_data]
            final_result = beginning_of_next_year - beginning_of_year

            print(final_result)


        elif what_time == "2":
            os.system("cls")


        elif what_time == "3":
            os.system("cls")


        elif what_time == "4":
            os.system("cls")
            number_of_people = main_data[-1][which_data]
            print(f"Przez cały okres pandemi : {number_of_people} osób")
            break

def search_date(date,main_data):
    """funkcja zwracajaca slownik listy ktory pasuje do naszej daty"""

    first = 0
    last = len(main_data) - 1
    mid = int((first + last)/2)

    check_date = main_data[mid]["Date"]
    check_date = check_date.split("T")
    check_date = check_date[0]

    while check_date != date:
        check_date = check_date.split("-")
        if type(date) == str:
            date = date.split("-")
        check_date = datetime.datetime(int(check_date[0]), int(check_date[1]), int(check_date[2]))
        date_time = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
        date = f"{date[0]}-{date[1]}-{date[2]}"

        if check_date < date_time:
            first = mid -1
            mid = int((first + last)/2)
            check_date = main_data[mid]["Date"]
            check_date = check_date.split("T")
            check_date = check_date[0]

        elif check_date > date_time:
            last = mid -1
            mid = int((first + last)/2)
            check_date = main_data[mid]["Date"]
            check_date = check_date.split("T")
            check_date = check_date[0]

    return main_data[mid]






main()