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
        self.longer_months = ["01", "03", "05", "07", "08", "10", "12"]
        self.shorter_months = ["04", "06", "09", "11"]

    def main(self):
        """metoda zarzadzajaca """

        while self.what_time in ("1", "2", "3", "4"):
            if self.what_time == "1":
                os.system("cls")
                year = input("Podaj rok ktory chcesz sprawdzić :")

                final_result = self.data_processing(year, "year")

                return final_result

            elif self.what_time == "2":
                os.system("cls")

                month = input("Podaj miesiąc  ktory chcesz sprawdzić (RRRR-MM):")
                final_result = self.data_processing(month, "month")

                return final_result

            elif self.what_time == "3":
                os.system("cls")

                day = input("Podaj dzień  ktory chcesz sprawdzić (RRRR-MM-DD):")
                final_result = self.make_date_for_day_request(day)

                if final_result < 0:
                    final_result = "Przepraszamy ale nie mamy danych do podanego zapytania"

                return final_result

            elif self.what_time == "4":
                os.system("cls")
                number_of_people = self.main_data[-1][self.what_data]
                print(f"Przez cały okres pandemi : {number_of_people} osób")
                break

    def data_processing(self, user_time, time):
        """funkcja przetwarzajaca dane od uzytkownika """

        data = self.make_date(user_time, time)

        beginning_of_year = self.search_date(data[0])
        end_of_year = self.search_date(data[1])

        beginning_of_year = beginning_of_year[self.what_data]
        end_of_year = end_of_year[self.what_data]

        final_result = end_of_year - beginning_of_year
        if final_result < 0:
            final_result = "Przepraszamy ale nie mamy danych do podanego zapytania"

        return final_result

    def make_date_for_day_request(self, user_day):
        """metoda zwracajaca liczbe dancy o ktore zapytał uzytkownik
            jezeli jego zapytanie dotyczylo konkretnego dnia"""

        time_range_data = ConnectionToData(self.country).time_range_for_day(self.main_data)
        while user_day not in time_range_data:
            user_day = input("Podałeś dzien spoza okresu pandemi, podaj poprawny : ")

        first_day_pandemic = self.main_data[0]["Date"]
        first_day_pandemic = first_day_pandemic.split("T")
        first_day_pandemic = first_day_pandemic[0]

        if user_day == first_day_pandemic:
            return self.main_data[0][self.what_data]
        else:
            user_day_split = user_day.split("-")
            if user_day_split[2] == "01" and user_day_split[1] == "01":
                previous_day = f"{int(user_day_split[0])-1}-12-31"

                previous_day = self.search_date(previous_day)
                user_day = self.search_date(user_day)

                previous_day = previous_day[self.what_data]
                user_day = user_day[self.what_data]

                return user_day - previous_day

            elif user_day_split[2] == "01":
                day = self.return_last_day_of_the_month(f"{user_day_split[0]}-0{int(user_day_split[1])-1}")

                if int(user_day_split[1])-1 < 10:
                    verified_month = f"0{int(user_day_split[1])-1}"
                else:
                    verified_month = int(user_day_split[1])-1

                previous_day = f"{user_day_split[0]}-{verified_month}-{day}"

                previous_day = self.search_date(previous_day)
                user_day = self.search_date(user_day)

                previous_day = previous_day[self.what_data]
                user_day = user_day[self.what_data]

                return user_day - previous_day

            else:
                day = int(user_day_split[2])-1
                if day < 10:
                    day = f"0{day}"

                previous_day = f"{user_day_split[0]}-{user_day_split[1]}-{day}"

                previous_day = self.search_date(previous_day)
                user_day = self.search_date(user_day)

                previous_day = previous_day[self.what_data]
                user_day = user_day[self.what_data]

                return user_day - previous_day

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
        """metoda sprawdza czy podany rok lub miesiac jest z okresu pandemi
        oraz zwraca przetworzone daty poczatku i konca okresu ktorego szukamy"""

        time_range_data = ConnectionToData(self.country).time_range_pandemic(self.main_data, time_range)

        while user_data not in time_range_data:
            user_data = input("Podałeś czas spoza okresu pandemi, podaj poprawny : ")

        if time_range == "year":
            if user_data == self.return_last_or_first_date(0, time_range):
                first_day = self.return_last_or_first_date(0, "day")
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
                first_day = self.return_last_or_first_date(0, "day")
                day = self.return_last_day_of_the_month(user_data)
                last_day = f"{user_data}-{day}"

            elif user_data == self.return_last_or_first_date(-1, time_range):
                first_day = f"{user_data}-01"
                last_day = self.main_data[-1]["Date"]
                last_day = last_day.split("T")
                last_day = last_day[0]

            else:
                first_day = f"{user_data}-01"
                day = self.return_last_day_of_the_month(user_data)
                last_day = f"{user_data}-{day}"

            return [first_day, last_day]

    def return_last_day_of_the_month(self, user_data):
        """metoda sprawdzajaca jaki jest ostatni dzien podanego przez uzytkownika miesiaca"""

        user_data = user_data.split("-")
        if user_data[1] in self.longer_months:
            day = 31
            return day

        elif user_data[1] in self.shorter_months:
            day = 30
            return day

        elif user_data[1] == "02":
            if int(user_data[0]) % 4 == 0:
                day = 29
            else:
                day = 28
            return day
