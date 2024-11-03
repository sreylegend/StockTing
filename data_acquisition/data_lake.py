import pandas as pd
from pathlib import Path
import json
from datetime import datetime
import logging
from typing import Dict, Any, Union

logger = logging.getLogger(__name__)

class DataLake:
    def __init__(self, base_path: str = "data"):
        self.base_path = Path(base_path)
        self._create_directories()

    def _create_directories(self):
        """Create necessary directories for data storage"""
        directories = ['market_data', 'economic_data', 'news_data', 'fundamentals']
        for dir_name in directories:
            (self.base_path / dir_name).mkdir(parents=True, exist_ok=True)

    def save_market_data(self, data: Dict[str, pd.DataFrame]):
        """Save market data to parquet files"""
        for ticker, df in data.items():
            try:
                file_path = self.base_path / 'market_data' / f"{ticker}_{datetime.now().date()}.parquet"
                df.to_parquet(file_path)
                logger.info(f"Saved market data for {ticker}")
            except Exception as e:
                logger.error(f"Error saving market data for {ticker}: {str(e)}")

    def save_economic_data(self, data: Dict[str, pd.Series]):
        """Save economic indicators data"""
        try:
            df = pd.DataFrame(data)
            file_path = self.base_path / 'economic_data' / f"economic_indicators_{datetime.now().date()}.parquet"
            df.to_parquet(file_path)
            logger.info("Saved economic data")
        except Exception as e:
            logger.error(f"Error saving economic data: {str(e)}")

    def save_news_data(self, articles: list):
        """Save news articles data"""
        try:
            file_path = self.base_path / 'news_data' / f"news_{datetime.now().date()}.json"
            with open(file_path, 'w') as f:
                json.dump(articles, f)
            logger.info("Saved news data")
        except Exception as e:
            logger.error(f"Error saving news data: {str(e)}")

    def save_fundamentals(self, data: Dict[str, Dict]):
        """Save fundamental data"""
        try:
            file_path = self.base_path / 'fundamentals' / f"fundamentals_{datetime.now().date()}.json"
            with open(file_path, 'w') as f:
                json.dump(data, f)
            logger.info("Saved fundamentals data")
        except Exception as e:
            logger.error(f"Error saving fundamentals data: {str(e)}") 