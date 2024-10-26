from fastapi import APIRouter, Depends, HTTPException, Request
from typing import List, Annotated

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

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


templates = Jinja2Templates(directory="templates")

@products_router.get("/html", response_class=HTMLResponse)
def get_stores_html(
    request: Request,
    product_service: ProductService = Depends(get_product_service)
):
    products = product_service.get_all_products()
    return templates.TemplateResponse("product.html", {"request": request, "products": products})