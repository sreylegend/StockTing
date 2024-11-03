from typing import Dict, List
import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
YAHOO_FINANCE_TICKERS: List[str] = [
    "SPY",  # S&P 500 ETF
    "QQQ",  # NASDAQ ETF
    "AAPL", "MSFT", "GOOGL", "AMZN", "META",  # Tech giants
    "JPM", "BAC", "GS",  # Financial sector
    "JNJ", "PFE", "UNH",  # Healthcare sector
]

# FRED API Configuration
FRED_API_KEY: str = os.getenv("FRED_API_KEY", "")
FRED_INDICATORS: Dict[str, str] = {
    "GDP": "GDP",                    # Gross Domestic Product
    "UNRATE": "UNRATE",             # Unemployment Rate
    "CPIAUCSL": "CPIAUCSL",         # Consumer Price Index
    "FEDFUNDS": "FEDFUNDS",         # Federal Funds Rate
    "T10Y2Y": "T10Y2Y",             # Treasury Yield Spread
}

# News API Configuration
NEWS_API_KEY: str = os.getenv("NEWS_API_KEY", "")
NEWS_SOURCES: List[str] = [
    "reuters",
    "bloomberg",
    "financial-times",
    "business-insider",
    "wall-street-journal",
] 