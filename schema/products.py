from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    price: float

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    name: str | None
    price: float | None

class Product(ProductBase):
    product_id: int

    class Config:
        from_attributes = True
