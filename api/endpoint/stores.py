from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated, List
from service.stores import StoreService
from api.dependecies import get_store_service
from schema.stores import Store
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

stores_router = APIRouter()

CommonStoreService = Annotated[
    StoreService,
    Depends(get_store_service)
]

@stores_router.get("/stores", response_model=List[Store])
def get_stores(
    store_service: StoreService = Depends(get_store_service)
):
    return store_service.get_all_stores()

templates = Jinja2Templates(directory="templates")

@stores_router.get("/html", response_class=HTMLResponse)
def get_stores_html(
    request: Request,
    store_service: StoreService = Depends(get_store_service)
):
    stores = store_service.get_all_stores()
    return templates.TemplateResponse("stores.html", {"request": request, "stores": stores})