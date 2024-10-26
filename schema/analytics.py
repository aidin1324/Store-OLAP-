from pydantic import BaseModel
from datetime import datetime

class SaleData(BaseModel):
        date: datetime
        store_name: str
        product_name: str
        quantity: int


class AnalyticsOutput(BaseModel):
    total_quantity: int
    total_amount: float
    sales_data: list[SaleData]
