import requests


class ConnectionToData:
    """klasa słuzacza do pobrania danych """

    def __init__(self, country):
        self.API_URL_COUNTRY = "https://api.covid19api.com/dayone/country/"
        self.country = country

    def make_main_data(self):
        """polaczeni sie z glownymi danymi """

        while self.country not in self.make_list_of_countries():
            self.country = input("Nie znaleziono kraju, jakie panstwo chcesz sprawdzić? ANG: ")
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

    def time_range_years(self, main_data):
        """metoda okreslajaca ramy czasowe pandemi"""

        years = []
        for day in main_data:
            day = day["Date"]
            day = day.split("T")
            day = day[0]
            day = day.split("-")
            years.append(day[0])
        years = set(years)

        return years

