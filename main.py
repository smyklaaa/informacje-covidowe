import os
from connection_to_data import ConnectionToData
from check_data import CheckData

print("Zródło danych: https://covid19api.com/")


def main():
    while True:
        country = input("Jakie panstwo chcesz sprawdzić? ANG: ").title()
        main_data = ConnectionToData(country)
        main_data = main_data.make_main_data()

        while True:
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

                    what_next = "Confirmed"

                    result = CheckData(what_time, main_data, country, what_next).main()
                    if what_time in ("1", "2", "3"):
                        print(f"Suma zakażeń w podanym okresie: {result}")
                    break

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
                    result = CheckData(what_time, main_data, country, what_next).main()
                    if what_time in ("1", "2", "3"):
                        print(f"Suma zgonow w podanym okresie: {result}")
                    break

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
                    result = CheckData(what_time, main_data, country, what_next).main()
                    if what_time in ("1", "2", "3"):
                        print(f"Suma osób które wyzdrowiały w podanym okresie: {result}")
                    break

            go_on = input("Czy chcesz kontynuowac sprawdzanie? t/n: ")
            if go_on == "t":
                os.system("cls")
            else:
                os.system("cls")
                break

        go_on = input("Czy chcesz wybrac inne panstwo? t/n: ")
        if go_on == "t":
            os.system("cls")
        else:
            break

main()
