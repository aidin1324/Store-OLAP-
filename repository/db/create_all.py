from sqlite3 import connect

def create_all(path):
    with connect(path) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS stores (
            store_id INTEGER PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            address VARCHAR(255),
            working_time VARCHAR(50)
            );
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            product VARCHAR(100) NOT NULL,
            price DECIMAL(10, 2) NOT NULL
            );
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
            sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE NOT NULL,
            product_id INTEGER,
            store_id INTEGER,
            quantity INTEGER NOT NULL,
            FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
            FOREIGN KEY (store_id) REFERENCES stores(store_id) ON DELETE CASCADE   
        );
        ''')
        conn.commit()    
        print('Tables created successfully!')
