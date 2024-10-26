from .base import BaseRepository
import sqlite3
from schema.stores import StoreCreate, StoreUpdate, Store

class StoreRepository(BaseRepository):

    def __init__(self, conn):
        super().__init__(conn)
        self.cursor = self.connection.cursor()
        
    def get_store(self, store_id) -> Store:
        self.cursor.execute('SELECT * FROM stores WHERE store_id = ?', (store_id,))
        result = self.cursor.fetchone()
        if result:
            return Store(**result)
        return None

    def get_all_stores(self) -> list[Store]:
        self.cursor.execute('SELECT * FROM stores')
        results = self.cursor.fetchall()

        stores = [
            Store(
                store_id=result[0],
                name=result[1],
                address=result[2],
                working_time=result[3]
            ) for result in results
        ]

        return stores
    
    def post_store(self, store: StoreCreate):
        self.cursor.execute(
            'INSERT INTO stores (name, address, working_time) VALUES (?, ?, ?)', 
            (store.name, store.address, store.working_time)
        )
        self.connection.commit()

    def update_store(self, store_id, store: StoreUpdate):
        if store.name:
            self.cursor.execute('UPDATE stores SET name = ? WHERE store_id = ?', (store.name, store_id))
        if store.address:
            self.cursor.execute('UPDATE stores SET address = ? WHERE store_id = ?', (store.address, store_id))
        if store.working_time:
            self.cursor.execute('UPDATE stores SET working_time = ? WHERE store_id = ?', (store.working_time, store_id))
        self.connection.commit()

    def delete_store(self, store_id):
        self.cursor.execute('DELETE FROM stores WHERE store_id = ?', (store_id,))
        self.connection.commit()
