import os
from connection_to_data import ConnectionToData
from confirmed import Confirmed


def main():
    country = input("Jakie panstwo chcesz sprawdzić? ANG: ")
    main_data = ConnectionToData(country)
    main_data = main_data.make_main_data()

    what_next = input("Wpisz numer danych które chcesz sprawdzić:\n"
                      "(1)Zakażenia\n(2)Zgony\n(3)Ozdrowieńcy\n")
    while what_next not in ("1", "2", "3"):
        print("Niepoprawne zapytanie")
        what_next = input("Wpisz numer danych które chcesz sprawdzić:\n"
                          "(1)Zakażenia\n(2)Zgony\n(3)Ozdrowieńcy\n")

    while what_next in ("1", "2", "3"):

        if what_next == "1":
            os.system("cls")
            what_time = input("Wpisz numer danych okresu który chcesz sprawdzić:\n"
                              "(1)Suma w ciagu roku\n(2)Suma w ciągu miesiaca\n"
                              "(3)Suma w ciągu dnia\n(4)Cały okres pandemi\n")

            while what_time not in ("1", "2", "3", "4"):
                print("Niepoprawne zapytanie")
                what_time = input("Wpisz numer danych okresu który chcesz sprawdzić:\n"
                                  "(1)Suma w ciagu roku\n(2)Suma w ciągu miesiaca\n"
                                  "(3)Suma w ciągu dnia\n(4)Cały okres pandemi\n")

            result = Confirmed(what_time, main_data, country).main()
            print(f"Suma zakażeń w podanym roku: {result}")



        elif what_next == "2":
            os.system("cls")
            what_time = input("Wpisz numer danych które chcesz sprawdzić:\n"
                              "(1)Suma w ciagu roku\n(2)Suma w ciągu miesiaca\n"
                              "(3)Suma w ciągu dnia\n(4)Cały okres pandemi\n")

            while what_time not in ("1", "2", "3", "4"):
                print("Niepoprawne zapytanie")
                what_time = input("Wpisz numer danych okresu który chcesz sprawdzić:\n"
                                  "(1)Suma w ciagu roku\n(2)Suma w ciągu miesiaca\n"
                                  "(3)Suma w ciągu dnia\n(4)Cały okres pandemi\n")

            what_next = "Deaths"

        elif what_next == "3":
            os.system("cls")
            what_time = input("Wpisz numer danych które chcesz sprawdzić:\n"
                              "(1)Suma w ciagu roku\n(2)Suma w ciągu miesiaca\n"
                              "(3)Suma w ciągu dnia\n(4)Cały okres pandemi\n")

            while what_time not in ("1", "2", "3", "4"):
                print("Niepoprawne zapytanie")
                what_time = input("Wpisz numer danych okresu który chcesz sprawdzić:\n"
                                  "(1)Suma w ciagu roku\n(2)Suma w ciągu miesiaca\n"
                                  "(3)Suma w ciągu dnia\n(4)Cały okres pandemi\n")

            what_next = "Recovered"

main()