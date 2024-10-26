import sqlite3
from .config import db_path

def get_connection():
    try:
        connection = sqlite3.connect(db_path)
        return connection
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
        return None
