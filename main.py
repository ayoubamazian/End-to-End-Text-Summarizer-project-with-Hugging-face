import sys
from textSummarizer.logging import logging
from textSummarizer.exceptions import CustomException
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline

STAGE_NAME = 'Data Ingestion Stage'
STAGE_NAME_2 = 'Data Validation Stage'
try:
    logging.info(f"Stage {STAGE_NAME} started")
    data_ingestion = DataIngestionTrainPipeline()
    data_ingestion.main()
    logging.info(f"Stage {STAGE_NAME} completed")
    
    logging.info(f"Stage {STAGE_NAME_2} started")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logging.info(f"Stage {STAGE_NAME_2} completed")

except Exception as e:
    raise CustomException(e, sys)