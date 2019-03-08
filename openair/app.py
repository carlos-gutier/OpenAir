"""Main application and routing logic for OpenAQ."""
from flask import Flask, render_template, request
import requests
import openaq
import pandas
from .airdata import *

api = openaq.OpenAQ() 

def create_app():
    """Create and configure and instance of the Flask application"""
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    DB.init_app(app)


    @app.route('/')
    def home():
        return render_template('base.html')

    @app.route('/load')
    def db_load_city():
        df_city = api.cities(df=True)
        load_cities(df_city)
        return render_template('base.html', title='Cities Loaded')


    @app.route('/countries')
    def db_load_country():
        df_country = api.countries(df=True)
        load_countries(df_country)
        return render_template('base.html', title='Countries Loaded')


    return app