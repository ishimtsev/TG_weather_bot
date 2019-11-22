import pymongo
from pymongo import MongoClient
import json
from bson.json_util import dumps


client = MongoClient('localhost', 27017)
db = client['weather_bot']
collection = db['users']
print(collection.find_one({"cityname": "Тюмень"}))
# print(collection.find_one({"cityname": "Марсель"}).user)
temp=collection.find_one({"cityname": "Тюмень"})
# temp2=dumps(temp)
print(temp["state"])

# data=dumps(collection.find_one({"cityname": "Марсель"}))
# data2=json.loads(data)
# print(data)
# print((data.user))
