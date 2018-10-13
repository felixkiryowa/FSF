"""
This module defines api views

"""
import psycopg2
import datetime
import jwt
from flask import request
from flask import jsonify
from flask import make_response
from werkzeug.security import generate_password_hash ,check_password_hash
from functools import wraps


from flask import json
from flask import jsonify
from flask import request
from flask import Response
from flask.views import MethodView
# from token_required import token_required
from api.models.menu_model import OrderMenu

class Menu(MethodView):
    """Class to define all the menu api end points"""
   
    def  post(self):

        # Get send order
        new_menu_data = request.get_json()
     
        if('item_name' in new_menu_data and 'price' in new_menu_data and 'current_items' in new_menu_data):
            OrderMenu(new_menu_data['item_name'],new_menu_data['price'],new_menu_data['current_items']).execute_add_menu_item_query()  
            return jsonify({'Message':'New Menu Item Has Been  Created'}),201       
        else:
            menu_object = "{'item_name': 'Greens','price':50000,'current_items':40}"
            bad_menu_object = {
            "error": "Bad Menu Object",
            "help of the correct auth object format":menu_object
            }
            response = Response(
                json.dumps(bad_menu_object),
                status=400, mimetype="application/json"
                )
            return response

    def get(self):
        menu = OrderMenu.get_menu()
        
        columns = ('item_id','item_name', 'price', 'current_items')
        results = []
        if menu:
            for row in menu:
                results.append(dict(zip(columns, row)))
            return jsonify({'Available Menu':results}),200


class MenuUrls:
    @staticmethod
    def fetch_menu_urls(app):
        # Register classes as views
        add_menu_item_view = Menu.as_view('order_menu')
        app.add_url_rule('/api/v2/menu', view_func=add_menu_item_view , methods=['POST','GET',])
