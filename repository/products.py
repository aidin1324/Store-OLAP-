from .base import BaseRepository
from schema.products import ProductCreate, ProductUpdate, Product


class ProductRepository(BaseRepository):
    def __init__(self, conn):
        super().__init__(conn)
        self.cursor = self.connection.cursor()
        
    def get_product(self, product_id: int) -> Product:
        self.cursor.execute('SELECT * FROM products WHERE product_id = ?', (product_id,))
        result = self.cursor.fetchone()
        if result:
            return Product(
                product_id=result[0],
                name=result[1],
                price=result[2]  
            )   
        return None

    def get_all_products(self) -> list[Product]:
        self.cursor.execute('SELECT * FROM products')
        results = self.cursor.fetchall()

        products = [Product(

            product_id=result[0],

            name=result[1],

            price=result[2]    

            ) for result in results

        ]

        return products
            
    
    def delete_product(self, product_id: int) -> None:
        self.cursor.execute('DELETE FROM products WHERE product_id = ?', (product_id,))
        self.connection.commit()

    def update_product(self, product_id: int, product_update: ProductUpdate) -> None:
        if product_update.name is not None:
            self.cursor.execute('UPDATE products SET name = ? WHERE product_id = ?', (product_update.name, product_id))
        if product_update.price is not None:
            self.cursor.execute('UPDATE products SET price = ? WHERE product_id = ?', (product_update.price, product_id))
        self.connection.commit()

    def post_product(self, product_create: ProductCreate) -> None:
        self.cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (product_create.name, product_create.price))
        self.connection.commit()
