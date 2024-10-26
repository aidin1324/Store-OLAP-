import pandas as pd
from datetime import datetime
from schema.analytics import SaleData, AnalyticsOutput
from repository.products import ProductRepository
from repository.sales import SaleRepository
from repository.stores import StoreRepository


class AnalyticsService:
    def __init__(
        self, 
        product_repository: ProductRepository,
        sale_repository: SaleRepository, 
        store_repository: StoreRepository
        ):
        self.product_repository = product_repository
        self.sale_repository = sale_repository
        self.store_repository = store_repository

    def get_total_sales(self):
        sales = pd.DataFrame(self.sale_repository.get_all_sales())
        products = pd.DataFrame(self.product_repository.get_all_products())
        merged_data = sales.merge(products, on='product_id')
        total_quantity = merged_data['quantity'].sum()
        total_amount = (merged_data['quantity'] * merged_data['price']).sum()
        return total_quantity, total_amount

    def filter_sales_data(self, start_date=None, end_date=None, store_name=None, product_name=None):
        sales = pd.DataFrame(self.sale_repository.get_all_sales())
        stores = pd.DataFrame(self.store_repository.get_all_stores())
        products = pd.DataFrame(self.product_repository.get_all_products())

        filtered_data = sales

        if start_date:
            filtered_data = filtered_data[filtered_data['date'] >= start_date]
        if end_date:
            filtered_data = filtered_data[filtered_data['date'] <= end_date]

        if store_name:
            store_ids = stores[stores['name'] == store_name]['store_id']
            filtered_data = filtered_data[filtered_data['store_id'].isin(store_ids)]

        if product_name:
            product_ids = products[products['name'] == product_name]['product_id']
            filtered_data = filtered_data[filtered_data['product_id'].isin(product_ids)]

        return filtered_data

    def display_sales_data(self, start_date=None, end_date=None, store_name=None, product_name=None) -> AnalyticsOutput:
        filtered_data = self.filter_sales_data(start_date, end_date, store_name, product_name)
        total_quantity, total_amount = self.get_total_sales()

        stores = pd.DataFrame(self.store_repository.get_all_stores())
        products = pd.DataFrame(self.product_repository.get_all_products())
        merged_data = filtered_data.merge(stores, on='store_id').merge(products, on='product_id')
        sales_data = [
            SaleData(
                date=row['date'],
                store_name=row['name_x'],
                product_name=row['name_y'],
                quantity=row['quantity']
            )
            for _, row in merged_data.iterrows()
        ]

        return AnalyticsOutput(
            total_quantity=total_quantity,
            total_amount=total_amount,
            sales_data=sales_data
        )