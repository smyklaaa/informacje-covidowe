import os
import datetime
from connection_to_data import ConnectionToData


class CheckData:
    """klasa zwracajaca dane o ktore zapytał uzytkownik"""

    def __init__(self, what_time, main_data, country, what_data):
        self.what_time = what_time
        self.main_data = main_data
        self.country = country
        self.what_data = what_data

    def main(self):
        """metoda zarzadzajaca """

        while self.what_time in ("1", "2", "3", "4"):
            if self.what_time == "1":
                os.system("cls")
                year = input("Podaj rok ktory chcesz sprawdzić : ")

                data = self.make_date(year, "year")

                beginning_of_year = self.search_date(data[0])
                end_of_year = self.search_date(data[1])

                beginning_of_year = beginning_of_year[self.what_data]
                end_of_year = end_of_year[self.what_data]

                final_result = end_of_year - beginning_of_year

                return final_result

            elif self.what_time == "2":
                os.system("cls")

                month = input("Podaj miesiąc  ktory chcesz sprawdzić (RRRR-MM): ")

                data = self.make_date(month, "month")     #DDDDDDDDDDDDDDDDDDDDDDDDDDD

                beginning_of_month = self.search_date(data[0])
                end_of_month = self.search_date(data[1])

                beginning_of_month = beginning_of_month[self.what_data]
                end_of_month = end_of_month[self.what_data]

                final_result = end_of_month - beginning_of_month

                return final_result

            elif self.what_time == "3":
                os.system("cls")

            elif self.what_time == "4":
                os.system("cls")
                number_of_people = self.main_data[-1][self.what_data]
                print(f"Przez cały okres pandemi : {number_of_people} osób")
                break

    def return_last_or_first_date(self, first_or_last, time_range):
        """metoda zwracajaca poczatkowa lub koncowa date pandemi dla roku lub miesiaca lub dnia"""

        date = self.main_data[first_or_last]["Date"]
        date = date.split("T")
        date = date[0]
        date = date.split("-")

        if time_range == "year":
            date = date[0]
            return str(date)
        elif time_range == "month":
            date = f"{date[0]}-{date[1]}"
            return date
        elif time_range == "day":
            date = f"{date[0]}-{date[1]}-{date[2]}"
            return date

    def search_date(self, date):
        """metoda zwracajaca slownik z listy głownych danych ktory pasuje do podanej daty"""

        first = 0
        last = len(self.main_data) - 1
        mid = int((first + last)/2)

        check_date = self.main_data[mid]["Date"]
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
                first = mid + 1
                mid = int((first + last)/2)
                check_date = self.main_data[mid]["Date"]
                check_date = check_date.split("T")
                check_date = check_date[0]

            elif check_date > date_time:
                last = mid - 1
                mid = int((first + last)/2)
                check_date = self.main_data[mid]["Date"]
                check_date = check_date.split("T")
                check_date = check_date[0]

        return self.main_data[mid]

    def make_date(self, user_data, time_range):
        """metoda sprawdza czy podany rok jest z okresu pandemi
        oraz zwraca przetworzone daty poczatku i konca okresu ktorego szukamy"""

        time_range_data = ConnectionToData(self.country).time_range_pandemic(self.main_data, time_range)

        while user_data not in time_range_data:
            user_data = input("Podałeś czas spoza okresu pandemi, podaj poprawny : ")

        if time_range == "year":
            if user_data == self.return_last_or_first_date(0, time_range):
                first_day = f"{user_data}-03-04"
                last_day = f"{user_data}-12-31"

            elif user_data == self.return_last_or_first_date(-1, time_range):
                first_day = f"{user_data}-01-01"
                last_day = self.main_data[-1]["Date"]
                last_day = last_day.split("T")
                last_day = last_day[0]

            else:
                first_day = f"{user_data}-01-01"
                last_day = f"{user_data}-12-31"

            return [first_day, last_day]

        elif time_range == "month":
            if user_data == self.return_last_or_first_date(0, time_range):
                first_day = f"{user_data}-04"
                last_day = f"{user_data}-31"

            elif user_data == self.return_last_or_first_date(-1, time_range):
                first_day = f"{user_data}-01"
                last_day = self.main_data[-1]["Date"]
                last_day = last_day.split("T")
                last_day = last_day[0]

            else:
                first_day = f"{user_data}-01"
                last_day = f"{user_data}-28"           #tu dałem bezpieczne dane ale to trzeba zmienic

            return [first_day, last_day]
