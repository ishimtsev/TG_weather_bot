import pymongo
from pymongo import MongoClient
import json
import config
import sqlite3

class SQLighter:

    def __init__(self):
        self.connection = sqlite3.connect(config.database)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    def select_all(self):
        """ Получаем все строки """
        with self.connection:
            return self.cursor.execute('SELECT * FROM users').fetchall()

    def get_user_state(self, user_id):
        with self.connection:
            sql = "SELECT state FROM users WHERE id = ?"
            return self.cursor.execute(sql, (user_id,)).fetchone()[0]

    def set_user_state(self, user_id, state):
        with self.connection:
            sql = "UPDATE users SET state = ? WHERE id = ?"
            self.cursor.execute(sql, (state, user_id))
            self.connection.commit()
            return


# get_user_state --
# set_user_state
# set_city
# add_user
# add_temp_results
# get_temp_results
# delete_temp_results

a=SQLighter()

a.set_user_state(139959859, 245)
print(a.get_user_state(139959859))



# client = MongoClient('localhost', 27017)
# db = client['weather_bot']
# collection = db['users']
#
# print(collection.find_one({"cityname": "Марсель"}))
#
# def get_state(user_id):
#     data = json.loads(collection.find_one({"user": user_id}))
#     if data is None:
#         return None
#     else:
#         return data["state"]
#
#
# def set_state(user_id, value):
#     with Vedis(config.db_file) as db:
#         try:
#             db[user_id] = value
#             return True
#         except:
#             return False