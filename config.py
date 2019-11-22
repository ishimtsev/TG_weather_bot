from enum import Enum
import keys

db_file = "database.vdb"


class States(Enum):
    S_START = "0"  # Начало нового диалога
    S_CITY_SEARCH = "1"
    S_CITY_FOUND = "2"
    S_CITY_OK = "3"

class Result_str(object):

    def __init__(self, number, city_name, city_key):
        self.number = number
        self.city_name = city_name
        self.city_key = city_key
