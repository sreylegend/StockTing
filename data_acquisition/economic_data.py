import pandas as pd
from fredapi import Fred
from typing import Dict, Optional
import logging

from .config import FRED_API_KEY, FRED_INDICATORS

logger = logging.getLogger(__name__)

class EconomicDataCollector:
    def __init__(self, api_key: str = FRED_API_KEY):
        self.fred = Fred(api_key=api_key)
        
    def fetch_economic_indicators(self) -> Dict[str, pd.Series]:
        """
        Fetch economic indicators from FRED
        """
        indicators = {}
        for indicator_name, series_id in FRED_INDICATORS.items():
            try:
                data = self.fred.get_series(series_id)
                if not data.empty:
                    indicators[indicator_name] = data
                    logger.info(f"Successfully fetched {indicator_name}")
                else:
                    logger.warning(f"No data available for {indicator_name}")
            except Exception as e:
                logger.error(f"Error fetching {indicator_name}: {str(e)}")
                
        return indicators

    def get_latest_values(self) -> Dict[str, float]:
        """
        Get the most recent values for all indicators
        """
        latest_values = {}
        for indicator_name, series_id in FRED_INDICATORS.items():
            try:
                data = self.fred.get_series(series_id)
                if not data.empty:
                    latest_values[indicator_name] = data.iloc[-1]
                    logger.info(f"Got latest value for {indicator_name}")
            except Exception as e:
                logger.error(f"Error getting latest value for {indicator_name}: {str(e)}")
                
        return latest_values 