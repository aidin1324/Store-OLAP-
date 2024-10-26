import sqlite3
import pandas as pd

def load_csv_to_db(csv_path, table_name, db_path):
    '''
        Example usage:
        load_csv_to_db('/path/to/stores.csv', 'stores')
        load_csv_to_db('/path/to/products.csv', 'products')
        load_csv_to_db('/path/to/sales.csv', 'sales')
    '''
    conn = sqlite3.connect(db_path)
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    
