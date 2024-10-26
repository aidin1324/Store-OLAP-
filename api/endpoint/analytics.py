from fastapi import APIRouter
from fastapi import Depends

from api.dependecies import get_analytics_service
from service.analytics import AnalyticsService

from schema.analytics import AnalyticsOutput
from typing import Annotated

analytics_router = APIRouter()

CommonAnalyticsService = Annotated[
    AnalyticsService,
    Depends(get_analytics_service)
]

@analytics_router.get("/analytics", response_model=AnalyticsOutput)
def get_analytics(
    analytics_service: CommonAnalyticsService,
    start_date: str | None = None,
    end_date: str | None = None,
    store_name: str | None = None,
    product_name: str | None = None,
):
    return analytics_service.show_basic_analysis(
        start_date=start_date,
        end_date=end_date,
        store_name=store_name,
        product_name=product_name
    )
