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

                years = ConnectionToData(self.country).time_range_years(self.main_data)

                while year not in years:
                    year = input("Podałeś rok spoza okresu pandemi, podaj poprawny : ")

                if year == self.return_year_from_last_date(0):
                    first_day_year = f"{year}-03-04"
                    last_day_year = f"{year}-12-31"

                elif year == self.return_year_from_last_date(-1):
                    first_day_year = f"{year}-01-01"
                    last_day_year = self.main_data[-1]["Date"]
                    last_day_year = last_day_year.split("T")
                    last_day_year = last_day_year[0]

                else:
                    first_day_year = f"{year}-01-01"
                    last_day_year = f"{year}-12-31"

                beginning_of_year = self.search_date(first_day_year)
                beginning_of_next_year = self.search_date(last_day_year)

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

    def return_year_from_last_date(self, first_or_last):
        year = self.main_data[first_or_last]["Date"]
        year = year.split("T")
        year = year[0]
        year = year.split("-")
        year = year[0]
        return str(year)

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

