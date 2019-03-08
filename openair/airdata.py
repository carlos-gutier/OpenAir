"""Retrieve Tweets, embeddings, and persist in the database."""
import pandas
from decouple import config
from .models import DB, Country, City


def load_cities(df_city):
    """Add or update a user *and* their Tweets, error if no/private user."""
    #DB.create_all()
    for index, row in df_city.iterrows():
        cities = City(name=row['city'], country_code=row['country'], count=row['count'], locations=row['locations'])
        DB.session.add(cities)
    DB.session.commit()


def load_countries(df_country):
    """Add or update a user *and* their Tweets, error if no/private user."""
    #DB.create_all()
    for index, row in df_country.iterrows():
        countries = Country(name=row['name'], count=row['count'], code=row['code'])
        DB.session.add(countries)
    DB.session.commit()