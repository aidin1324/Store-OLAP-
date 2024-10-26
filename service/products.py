from fastapi.exceptions import HTTPException
from repository.products import ProductRepository
from schema.products import ProductCreate, ProductUpdate, Product

class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def get_all_products(self) -> list[Product]:
        try:
            return self.product_repository.get_all_products()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))