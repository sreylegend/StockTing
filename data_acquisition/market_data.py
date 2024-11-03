import yfinance as yf
import pandas as pd
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import logging

from .config import YAHOO_FINANCE_TICKERS

logger = logging.getLogger(__name__)

class MarketDataCollector:
    def __init__(self, tickers: List[str] = YAHOO_FINANCE_TICKERS):
        self.tickers = tickers

    def fetch_historical_data(
        self,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        period: str = "1y"
    ) -> Dict[str, pd.DataFrame]:
        """
        Fetch historical market data for the specified tickers
        """
        if not start_date:
            start_date = datetime.now() - timedelta(days=365)
        if not end_date:
            end_date = datetime.now()

        data = {}
        for ticker in self.tickers:
            try:
                stock = yf.Ticker(ticker)
                df = stock.history(start=start_date, end=end_date)
                if not df.empty:
                    data[ticker] = df
                    logger.info(f"Successfully fetched data for {ticker}")
                else:
                    logger.warning(f"No data available for {ticker}")
            except Exception as e:
                logger.error(f"Error fetching data for {ticker}: {str(e)}")

        return data

    def fetch_fundamentals(self) -> Dict[str, Dict]:
        """
        Fetch fundamental data for the specified tickers
        """
        fundamentals = {}
        for ticker in self.tickers:
            try:
                stock = yf.Ticker(ticker)
                fundamentals[ticker] = {
                    'info': stock.info,
                    'financials': stock.financials.to_dict() if hasattr(stock, 'financials') else {},
                    'balance_sheet': stock.balance_sheet.to_dict() if hasattr(stock, 'balance_sheet') else {},
                    'cash_flow': stock.cashflow.to_dict() if hasattr(stock, 'cashflow') else {},
                }
                logger.info(f"Successfully fetched fundamentals for {ticker}")
            except Exception as e:
                logger.error(f"Error fetching fundamentals for {ticker}: {str(e)}")

        return fundamentals 