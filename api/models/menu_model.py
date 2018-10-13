from api import conn
from flask import jsonify

cur = conn.cursor()


class OrderMenu(object):

    cur.execute(
          """
            CREATE TABLE IF NOT EXISTS menu (
                    item_id SERIAL PRIMARY KEY,
                    item_name VARCHAR(255) NOT NULL,
                    price BIGINT NOT NULL,
                    current_items BIGINT NOT NULL
            )
            """
    )

    def __init__(self,item_name,price,current_items):
        self.item_name = item_name
        self.price = price
        self.current_items = current_items



    def execute_add_menu_item_query(self):
        cur = conn.cursor()
        sql = """INSERT INTO menu(item_name,price,current_items)
                VALUES(%s,%s,%s) RETURNING item_id;"""

        # execute the INSERT statement
        cur.execute(sql, (self.item_name, self.price, self.current_items,))
        # commit the changes to the database
        conn.commit()
        

    @staticmethod
    def get_menu():
            cur = conn.cursor()
            cur.execute("SELECT * FROM menu ORDER BY item_id")
            available_menu = cur.fetchall()
            
            return available_menu
          
     

