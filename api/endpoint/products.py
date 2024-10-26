from fastapi import APIRouter, Depends, HTTPException
from typing import List, Annotated

from service.products import ProductService
from api.dependecies import get_product_service

from schema.products import Product

products_router = APIRouter()

CommonProductService = Annotated[
    ProductService,
    Depends(get_product_service)
]

@products_router.get("/products", response_model=List[Product])
def get_products(
    product_service: ProductService = Depends(get_product_service)
):
    return product_service.get_all_products()
