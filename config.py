from enum import Enum
import keys

# token = "1234567:ABCxyz"
# db_file = "database.vdb"


class States(Enum):
    S_START = "0"  # Начало нового диалога
    S_ENTER_NAME = "1"
    S_ENTER_AGE = "2"
    S_SEND_PIC = "3"