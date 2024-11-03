#!/usr/bin/env python3

import sys
import os
from datetime import datetime, timedelta
import logging

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from data_acquisition.main import DataAcquisitionPipeline

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('data_acquisition.log'),
        logging.StreamHandler()
    ]
)

def main():
    # Create pipeline instance
    pipeline = DataAcquisitionPipeline()
    
    # Set date range (optional)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)  # Get 1 year of data
    
    try:
        # Run the pipeline
        pipeline.run_pipeline(
            start_date=start_date,
            end_date=end_date
        )
    except Exception as e:
        logging.error(f"Pipeline failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 