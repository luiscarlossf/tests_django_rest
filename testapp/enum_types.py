import pycountry

class CountryList:
    @staticmethod
    def get_alpha_2_country():
        countries = {}
        for country in pycountry.countries:
            if hasattr(country, "alpha_2"):
                countries[country.name] = country.alpha_2

        return countries