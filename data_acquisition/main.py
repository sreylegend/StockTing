import logging
from datetime import datetime
from typing import Optional

from .market_data import MarketDataCollector
from .economic_data import EconomicDataCollector
from .news_data import NewsDataCollector
from .data_lake import DataLake

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataAcquisitionPipeline:
    def __init__(self):
        self.market_collector = MarketDataCollector()
        self.economic_collector = EconomicDataCollector()
        self.news_collector = NewsDataCollector()
        self.data_lake = DataLake()

    def run_pipeline(
        self,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ):
        """
        Run the complete data acquisition pipeline
        """
        try:
            # Collect market data
            logger.info("Collecting market data...")
            market_data = self.market_collector.fetch_historical_data(
                start_date=start_date,
                end_date=end_date
            )
            self.data_lake.save_market_data(market_data)

            # Collect fundamental data
            logger.info("Collecting fundamental data...")
            fundamentals = self.market_collector.fetch_fundamentals()
            self.data_lake.save_fundamentals(fundamentals)

            # Collect economic indicators
            logger.info("Collecting economic indicators...")
            economic_data = self.economic_collector.fetch_economic_indicators()
            self.data_lake.save_economic_data(economic_data)

            # Collect news data
            logger.info("Collecting news data...")
            news_data = self.news_collector.fetch_financial_news()
            self.data_lake.save_news_data(news_data)

            logger.info("Data acquisition pipeline completed successfully")

        except Exception as e:
            logger.error(f"Error in data acquisition pipeline: {str(e)}")
            raise

if __name__ == "__main__":
    pipeline = DataAcquisitionPipeline()
    pipeline.run_pipeline() 