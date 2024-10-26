from fastapi import Depends

from sqlite3 import Connection
from repository.db.db import get_connection
from repository.products import ProductRepository
from repository.sales import SaleRepository
from repository.stores import StoreRepository
from repository.analytics import AnalyticsRepository

from service.products import ProductService
from service.analytics import AnalyticsService
from service.stores import StoreService


def get_product_repository(
    conn: Connection = Depends(get_connection)
):
    return ProductRepository(conn)


def get_sale_repository(
    conn: Connection = Depends(get_connection)
):
    return SaleRepository(conn)


def get_store_repository(
    conn: Connection = Depends(get_connection)
):
    return StoreRepository(conn)


def get_analytics_repository(
    conn: Connection = Depends(get_connection)
):
    return AnalyticsRepository(conn)


def get_product_service(
    product_repository: ProductRepository = Depends(get_product_repository)
):
    return ProductService(product_repository)


def get_store_service(
    store_repository: StoreRepository = Depends(get_store_repository)
):
    return StoreService(store_repository)


def get_analytics_service(
    analytics_repository: AnalyticsRepository = Depends(get_analytics_repository)
):
    return AnalyticsService(analytics_repository)