from fastapi.exceptions import HTTPException
from repository.stores import StoreRepository
from schema.stores import StoreCreate, StoreUpdate, Store

class StoreService:
    def __init__(self, store_repository: StoreRepository):
        self.store_repository = store_repository

    def get_all_stores(self) -> list[Store]:
        try:
            return self.store_repository.get_all_stores()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        