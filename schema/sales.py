from pydantic import BaseModel
from datetime import date

class SaleBase(BaseModel):
    date: date
    product_id: int
    store_id: int
    quantity: int

class SaleCreate(SaleBase):
    pass

class SaleUpdate(SaleBase):
    date: date | None
    product_id: int | None
    store_id: int | None
    quantity: int | None

class Sale(SaleBase):
    sale_id: int

    class Config:
        from_attributes = True