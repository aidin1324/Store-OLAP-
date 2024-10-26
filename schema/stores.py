from pydantic import BaseModel
from datetime import date

class StoreBase(BaseModel):
    name: str
    address: str
    working_time: str

class StoreCreate(StoreBase):
    pass

class StoreUpdate(StoreBase):
    name: str | None
    address: str | None
    working_time: str | None

class Store(StoreBase):
    store_id: int

    class Config:
        from_attributes = True
