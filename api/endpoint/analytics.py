from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import HTMLResponse

from api.dependecies import get_analytics_service
from service.analytics import AnalyticsService

from schema.analytics import AnalyticsOutput
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi import Request

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
        start_date=start_date.strip(),
        end_date=end_date.strip(),
        store_name=store_name.strip(),
        product_name=product_name.strip()
    )

templates = Jinja2Templates(directory="templates")

@analytics_router.get("/html", response_class=HTMLResponse)
def render_analytics_template(
    request: Request,
    analytics_service: CommonAnalyticsService,
    start_date: str | None = None,
    end_date: str | None = None,
    store_name: str | None = None,
    product_name: str | None = None,
):
    analysis_data = analytics_service.show_basic_analysis(
        start_date=start_date.strip() if start_date else None,
        end_date=end_date.strip() if end_date else None,
        store_name=store_name.strip() if store_name else None,
        product_name=product_name.strip() if product_name else None
    )
    
    return templates.TemplateResponse("analysis.html", {
        "request": request,
        "total_sales": analysis_data.total_sales,
        "total_amount": analysis_data.total_amount,
        "grouped_by_stores": analysis_data.grouped_by_stores,
        "start_date": start_date,
        "end_date": end_date,
        "store_name": store_name,
        "product_name": product_name
    })
