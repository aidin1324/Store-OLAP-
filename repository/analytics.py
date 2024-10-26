from .base import BaseRepository
import sqlite3
from sqlite3 import Connection

from schema.analytics import ShowData, AnalyticsOutput


class AnalyticsRepository(BaseRepository):
    
    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.cursor = self.connection.cursor()
        
    
    def filter_sales_data(
        self, 
        start_date: str = None, 
        end_date: str = None, 
        store_name: str = None, 
        product_name: str = None
    ) -> list[ShowData]:
        query = """
            SELECT s.date, st.name, s.quantity, SUM(s.quantity * p.price) as total_quantity
            FROM sales as s
            LEFT JOIN products as p ON s.product_id = p.product_id
            LEFT JOIN stores as st ON s.store_id = st.store_id
            WHERE 1 = 1
        """
        params = []
        
        if start_date:
            query += " AND s.date >= ?"
            params.append(start_date)
        
        if end_date:
            query += " AND s.date <= ?"
            params.append(end_date)
        
        if store_name:
            query += " AND st.name = ?"
            params.append(store_name)
        
        if product_name:
            query += " AND p.name = ?"
            params.append(product_name)
        
        query += " GROUP BY st.name ORDER BY st.name"
        
        self.cursor.execute(query, params)
        sales_data = self.cursor.fetchall()
        total_sales = sum([e[2] for e in sales_data])
        total_amount = sum([e[3] for e in sales_data])
        return AnalyticsOutput(
            total_sales=total_sales,
            total_amount=total_amount,
            grouped_by_stores=
            [
                ShowData(
                    store_name=e[1],
                    date=e[0],
                    quantity_sold=e[3],
                    total_sales = total_sales,
                    total_amount = total_amount
                )
                for e in sales_data
            ]
        )
