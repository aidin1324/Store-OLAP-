from fastapi import FastAPI
from api import api_router

from repository.db import config

app = FastAPI()
config.run_db_config()

app.include_router(api_router)
