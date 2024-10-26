from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated, List
from service.stores import StoreService
from api.dependecies import get_store_service
from schema.stores import Store

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
