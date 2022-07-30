import requests


class ConnectionToData:
    """klasa słuzacza do pobrania danych """

    def __init__(self, country):
        self.API_URL_COUNTRY = "https://api.covid19api.com/dayone/country/"
        self.country = country

    def make_main_data(self):
        """polaczeni sie z glownymi danymi """

        while self.country not in self.make_list_of_countries():
            self.country = input("Nie znaleziono kraju, jakie panstwo chcesz sprawdzić? ANG: ").title()
        response = requests.get(f"{self.API_URL_COUNTRY}{self.country}")
        main_data = response.json()
        return main_data

    def make_list_of_countries(self):
        """tworzenie listy panstw dostepnych w bazie danych"""

        response = requests.get("https://api.covid19api.com/countries")
        data = response.json()
        list_of_countries = []
        for country in data:
            list_of_countries.append(country["Country"])
        return list_of_countries

    def time_range_pandemic(self, main_data, time):
        """metoda okreslajaca ramy czasowe pandemi"""

        unique_values = []
        for day in main_data:
            day = day["Date"]
            day = day.split("T")
            day = day[0]
            day = day.split("-")
            if time == "year":
                unique_values.append(day[0])
            elif time == "month":
                unique_values.append(f"{day[0]}-{day[1]}")
        unique_values = set(unique_values)

        return unique_values

    def time_range_for_day(self, main_data):
        """metoda zwracajaca liste wszystkich dni pandemi"""

        days = []
        for day in main_data:
            day = day["Date"]
            day = day.split("T")
            day = day[0]
            days.append(day)

        return days



