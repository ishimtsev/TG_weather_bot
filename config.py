from enum import Enum

database = "database.db"


class States(Enum):
    S_START = "0"  # Начало нового диалога
    S_CITY_SEARCH = "1"
    S_CITY_FOUND = "2"
    S_CITY_OK = "3"


class Result_str(object):

    def __init__(self, number, city_name, city_key, full_str):
        self.number = number
        self.city_name = city_name
        self.city_key = city_key
        self.full_str = full_str
