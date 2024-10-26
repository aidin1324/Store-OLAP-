from pydantic import BaseModel
from datetime import datetime

class SaleData(BaseModel):
        date: datetime
        store_name: str
        product_name: str
        quantity: int


class ShowData(BaseModel):
    date: datetime
    store_name: str
    quantity_sold: float
    

class AnalyticsOutput(BaseModel):
    total_sales: float
    total_amount: float
    grouped_by_stores: list[ShowData]