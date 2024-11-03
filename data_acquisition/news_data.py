import requests
from typing import List, Dict
from datetime import datetime, timedelta
import logging

from .config import NEWS_API_KEY, NEWS_SOURCES

logger = logging.getLogger(__name__)

class NewsDataCollector:
    def __init__(self, api_key: str = NEWS_API_KEY):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2/"

    def fetch_financial_news(
        self,
        days_back: int = 7,
        sources: List[str] = NEWS_SOURCES
    ) -> List[Dict]:
        """
        Fetch financial news articles from specified sources
        """
        try:
            end_date = datetime.now()
            start_date = end_date - timedelta(days=days_back)
            
            params = {
                'apiKey': self.api_key,
                'sources': ','.join(sources),
                'from': start_date.isoformat(),
                'to': end_date.isoformat(),
                'language': 'en',
                'sortBy': 'publishedAt',
                'q': 'finance OR stock market OR trading'
            }
            
            response = requests.get(f"{self.base_url}everything", params=params)
            response.raise_for_status()
            
            articles = response.json().get('articles', [])
            logger.info(f"Successfully fetched {len(articles)} news articles")
            return articles
            
        except Exception as e:
            logger.error(f"Error fetching news data: {str(e)}")
            return [] 