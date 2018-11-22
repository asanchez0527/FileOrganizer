import sqlite3
from sqlite3 import Error


# connects to the db file located in the source folder
def connect(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
    return None
