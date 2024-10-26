from .create_all import create_all
from .script import load_csv_to_db

db_path = 'db.sqlite3'


def run_db_config():
    
    create_all(db_path)
    load_csv_to_db('data/stores.csv', 'stores', db_path)
    load_csv_to_db('data/products.csv', 'products', db_path)
    load_csv_to_db('data/sales.csv', 'sales', db_path)
    print('Database configured successfully')