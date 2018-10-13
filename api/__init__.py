import psycopg2
from flask import Flask
app = Flask(__name__)

conn = psycopg2.connect(database="Fast_food_fast",user="postgres",password="atagenda1@",host="localhost",port="5432")

from api.views.menu_views import MenuUrls
MenuUrls.fetch_menu_urls(app)