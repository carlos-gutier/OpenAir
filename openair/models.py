"""SQLAlchemy models for TwitOff"""
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class Country(DB.Model):
    """Coutries where OpenAQ collects air quality data."""
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(60), nullable=False)
    count = DB.Column(DB.Integer, nullable=False)
    code = DB.Column(DB.String(2), nullable=False)


class City(DB.Model):
    """Cities in Countries where OpenAQ collects air quality data."""
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(60), nullable=False)
    country_code = DB.Column(DB.Integer, DB.ForeignKey('country.id'), nullable=False)
    count = DB.Column(DB.Integer, nullable=False)
    locations = DB.Column(DB.Integer, nullable=False)

    