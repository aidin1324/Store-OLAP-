from .base import BaseRepository
import sqlite3

from schema.sales import SaleCreate, SaleUpdate, Sale

class SaleRepository(BaseRepository):

    def __init__(self, conn):
        super().__init__(conn)
        self.cursor = self.connection.cursor()

    def get_sale(self, sale_id) -> Sale:
        self.cursor.execute('SELECT * FROM sales WHERE sale_id = ?', (sale_id,))
        result = self.cursor.fetchone()
        if result:
            return Sale(**result)
        return None

    def get_all_sales(self, last_id: int = 0, limit: int = 10) -> list[Sale]:
        self.cursor.execute('SELECT * FROM sales WHERE sale_id > ? ORDER BY sale_id ASC LIMIT ?', (last_id, limit))
        results = self.cursor.fetchall()

        sales = [
            Sale(
                sale_id=result[0],
                date=result[1],
                product_id=result[2],
                store_id=result[3],
                quantity=result[4]
            ) for result in results
        ]

        return sales
    
    def post_sale(self, sale: SaleCreate):
        self.cursor.execute(
            'INSERT INTO sales (date, product_id, store_id, quantity) VALUES (?, ?, ?, ?)', 
            (sale.date, sale.product_id, sale.store_id, sale.quantity)
        )
        self.connection.commit()

    def update_sale(self, sale_id, sale: SaleUpdate):
        if sale.date:
            self.cursor.execute('UPDATE sales SET date = ? WHERE sale_id = ?', (sale.date, sale_id))
        if sale.product_id:
            self.cursor.execute('UPDATE sales SET product_id = ? WHERE sale_id = ?', (sale.product_id, sale_id))
        if sale.store_id:
            self.cursor.execute('UPDATE sales SET store_id = ? WHERE sale_id = ?', (sale.store_id, sale_id))
        if sale.quantity:
            self.cursor.execute('UPDATE sales SET quantity = ? WHERE sale_id = ?', (sale.quantity, sale_id))
        self.connection.commit()

    def delete_sale(self, sale_id):
        self.cursor.execute('DELETE FROM sales WHERE sale_id = ?', (sale_id,))
        self.connection.commit()
