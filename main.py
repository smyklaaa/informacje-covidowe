import os
import datetime
from connection_to_data import ConnectionToData
from confirmed import Confirmed


def main():
    country = input("Jakie panstwo chcesz sprawdzić? ANG: ")
    main_data = ConnectionToData(country)
    main_data = main_data.make_main_data()

    what_next = input("Wpisz numer danych które chcesz sprawdzić:\n"
                      "(1)Zakażenia\n(2)Zgony\n(3)Ozdrowieńcy\n")

    while what_next in ("1","2","3"):

        if what_next == "1":
            os.system("cls")
            what_time = input("Wpisz numer danych okresu który chcesz sprawdzić:\n"
                              "(1)Suma w ciagu roku\n(2)Suma w ciągu miesiaca\n"
                              "(3)Suma w ciągu dnia\n(4)Cały okres pandemi\n")

            Confirmed(what_time, main_data, country).main()



        elif what_next == "2":
            os.system("cls")
            what_time = input("Wpisz numer danych które chcesz sprawdzić:\n"
                              "(1)Suma w ciagu roku\n(2)Suma w ciągu miesiaca\n"
                              "(3)Suma w ciągu dnia\n(4)Cały okres pandemi\n")
            what_next = "Deaths"
            #period_of_time(what_time, what_next, main_data)

        elif what_next == "3":
            os.system("cls")
            what_time = input("Wpisz numer danych które chcesz sprawdzić:\n"
                              "(1)Suma w ciagu roku\n(2)Suma w ciągu miesiaca\n"
                              "(3)Suma w ciągu dnia\n(4)Cały okres pandemi\n")
            what_next = "Recovered"
            #period_of_time(what_time, what_next, main_data)


# def period_of_time(what_time, which_data, main_data):
#     while what_time in ("1", "2", "3", "4"):
#         if what_time == "1":
#             os.system("cls")
#             year = input("Podaj rok ktory chcesz sprawdzić : ")
#             while len(year) > 4:
#                 year = input("Podałeś rok z pryszlosci podaj rok ktory chcesz sprawdzić : ")
#
#             #first_day_year = f"{year}-01-01"
#             first_day_year = check_pandemic(f"{year}-01-01", main_data)
#             first_day_next_year = f"{int(year)+1}-01-01"
#
#             beginning_of_year = search_date(first_day_year, main_data)
#             beginning_of_next_year = search_date(first_day_next_year, main_data)
#
#             beginning_of_year = beginning_of_year[which_data]
#             beginning_of_next_year = beginning_of_next_year[which_data]
#
#             final_result = beginning_of_next_year - beginning_of_year
#
#             print(final_result)
#
#         elif what_time == "2":
#             os.system("cls")
#
#         elif what_time == "3":
#             os.system("cls")
#
#         elif what_time == "4":
#             os.system("cls")
#             number_of_people = main_data[-1][which_data]
#             print(f"Przez cały okres pandemi : {number_of_people} osób")
#             break


# def search_date(date,main_data):
#     """funkcja zwracajaca slownik listy ktory pasuje do naszej daty"""
#
#     first = 0
#     last = len(main_data) - 1
#     mid = int((first + last)/2)
#
#     check_date = main_data[mid]["Date"]
#     check_date = check_date.split("T")
#     check_date = check_date[0]
#
#     while check_date != date:
#         check_date = check_date.split("-")
#         if type(date) == str:
#             date = date.split("-")
#         check_date = datetime.datetime(int(check_date[0]), int(check_date[1]), int(check_date[2]))
#         date_time = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
#         date = f"{date[0]}-{date[1]}-{date[2]}"
#
#         if check_date < date_time:
#             first = mid -1
#             mid = int((first + last)/2)
#             check_date = main_data[mid]["Date"]
#             check_date = check_date.split("T")
#             check_date = check_date[0]
#
#         elif check_date > date_time:
#             last = mid -1
#             mid = int((first + last)/2)
#             check_date = main_data[mid]["Date"]
#             check_date = check_date.split("T")
#             check_date = check_date[0]
#
#     return main_data[mid]


# def check_pandemic(date, main_data):
#     """funkcja sprawdza czy data podana przez uzytkownika pokrywa sie z pandemia"""
#
#     date = date.split("-")
#     date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
#     check_data = make_datetime(main_data[0]["Date"])
#
#
#     while date < check_data:
#         date = input("Podałes date z przed pandemi, podaj poprawny rok: ")
#         date = make_datetime(date)
#
#     while date > check_data:
#         date = input("Podałes date z przyszłosci, podaj poprawny rok: ")
#         while len(date) > 4:
#             date = input("Podałes date z przyszłosci, podaj poprawny rok: ")
#         date = make_datetime(date)
#
#         while date < check_data:
#             date = input("Podałes date z przed pandemi, podaj poprawny rok: ")
#             date = make_datetime(date)
#
#     return date



def check_year(date, main_data):
    """funkcja sprawdza czy caly rok o ktory pyta uzytkownik pokrywa sie z pandemia"""

    date = date.split("-")
    date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
    while date < main_data[0]["Date"]:
        date = input("Podałes date z przed pandemi, podaj poprawny rok: ")
    while date > main_data[-1]["Date"]:
        date = input("Podałes date z przyszłosci, podaj poprawny rok: ")
    return date


# def make_datetime(check_date):
#     """funkcja zwracajaca przekonwertowana date string na typ datatime"""
#
#     check_date = check_date.split("T")
#     print(check_date)
#     check_date = check_date[0]
#     check_date = check_date.split("-")
#     print(check_date)
#     check_date = datetime.datetime(int(check_date[0]), int(check_date[1]), int(check_date[2]))
#     return check_date



main()