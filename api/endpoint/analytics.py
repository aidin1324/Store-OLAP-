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
    analytics_service: CommonAnalyticsService
):
    return analytics_service.display_sales_data()
