from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from .analytics import analytics_router
from .products import products_router
from .stores import stores_router

api_router = APIRouter()

api_router.include_router(
    analytics_router,
    prefix="/analytics",
    tags=["analytics"]
)

api_router.include_router(
    products_router,
    prefix="/products",
    tags=["products"]
)

api_router.include_router(
    stores_router,
    prefix="/stores",
    tags=["stores"]
)
templates = Jinja2Templates(directory="templates")

@api_router.get("/")
def welcome_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
