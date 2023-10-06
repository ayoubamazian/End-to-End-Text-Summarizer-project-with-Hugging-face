import sys
from textSummarizer.logging import logging
from textSummarizer.exceptions import CustomException
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline

STAGE_NAME = 'Data Ingestion Stage'
try:
    logging.info(f"Stage {STAGE_NAME} started")
    data_ingestion = DataIngestionTrainPipeline()
    data_ingestion.main()
    logging.info(f"Stage {STAGE_NAME} completed")

except Exception as e:
    raise CustomException(e, sys)