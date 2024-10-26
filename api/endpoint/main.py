from fastapi import APIRouter
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

@api_router.get("/")
def welcome_page():
    return {"message": "Welcome to the API!"}
