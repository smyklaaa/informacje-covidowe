import os
import datetime
from connection_to_data import ConnectionToData


class Confirmed:
    def __init__(self, what_time, main_data, country):
        self.what_time = what_time
        self.main_data = main_data
        self.country = country

    def main(self):
        """metoda zarzadzajaca """

        while self.what_time in ("1", "2", "3", "4"):
            if self.what_time == "1":
                os.system("cls")
                year = input("Podaj rok ktory chcesz sprawdzić : ")
                while len(year) > 4:
                    year = input("Podałeś rok z pryszlosci podaj rok ktory chcesz sprawdzić : ")

                years = ConnectionToData().time_range_years()
                while year not in years:
                    year = input("Podałeś rok z pryszlosci podaj rok ktory chcesz sprawdzić : ")





                first_day_year = self.check_pandemic(f"{year}-01-01")
                first_day_next_year = f"{int(year)+1}-01-01"

                beginning_of_year = self.search_date(first_day_year)
                beginning_of_next_year = self.search_date(first_day_next_year)

                beginning_of_year = beginning_of_year["Confirmed"]
                beginning_of_next_year = beginning_of_next_year["Confirmed"]

                final_result = beginning_of_next_year - beginning_of_year

                return final_result

            elif self.what_time == "2":
                os.system("cls")

            elif self.what_time == "3":
                os.system("cls")

            elif self.what_time == "4":
                os.system("cls")
                number_of_people = self.main_data[-1]["Confirmed"]
                print(f"Przez cały okres pandemi : {number_of_people} osób")
                break

    def search_date(self, date):
        """metoda zwracajaca slownik listy ktory pasuje do naszej daty"""

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
                first = mid -1
                mid = int((first + last)/2)
                check_date = self.main_data[mid]["Date"]
                check_date = check_date.split("T")
                check_date = check_date[0]

            elif check_date > date_time:
                last = mid -1
                mid = int((first + last)/2)
                check_date = self.main_data[mid]["Date"]
                check_date = check_date.split("T")
                check_date = check_date[0]

        return self.main_data[mid]

    def check_pandemic(self, date):
        """funkcja sprawdza czy data podana przez uzytkownika pokrywa sie z pandemia"""



        date = date.split("-")
        date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
        check_data = self.make_datetime(self.main_data[0]["Date"])

        while date < check_data:
            date = input("Podałes date z przed pandemi, podaj poprawny rok: ")
            date = self.make_datetime(date)

        while date > check_data:
            date = input("Podałes date z przyszłosci, podaj poprawny rok: ")
            while len(date) > 4:
                date = input("Podałes date z przyszłosci, podaj poprawny rok: ")
            date = self.make_datetime(date)

            while date < check_data:
                date = input("Podałes date z przed pandemi, podaj poprawny rok: ")
                date = self.make_datetime(date)

        return date

    def make_datetime(self, check_date):
        """funkcja zwracajaca przekonwertowana date string na typ datatime"""

        check_date = check_date.split("T")
        print(check_date)
        check_date = check_date[0]
        check_date = check_date.split("-")
        print(check_date)
        check_date = datetime.datetime(int(check_date[0]), int(check_date[1]), int(check_date[2]))
        return check_date
