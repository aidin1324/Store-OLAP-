import pandas as pd
from datetime import datetime
from schema.analytics import SaleData, AnalyticsOutput

from fastapi import HTTPException
from repository.analytics import AnalyticsRepository, ShowData


class AnalyticsService:
    def __init__(
        self, 
        analytics_repository: AnalyticsRepository
        ):
        self.analytics_repository = analytics_repository
        

    def show_basic_analysis(
        self,
        start_date: str = None,
        end_date: str = None,
        store_name: str = None,
        product_name: str = None
    ) -> list[ShowData]:
        try:
            return self.analytics_repository.filter_sales_data(
                start_date=start_date,
                end_date=end_date,
                store_name=store_name,
                product_name=product_name
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))