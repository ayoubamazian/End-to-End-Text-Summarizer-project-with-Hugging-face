import sys
from textSummarizer.logging import logging
from textSummarizer.exceptions import CustomException
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline

STAGE_NAME_1 = 'Data Ingestion Stage'
STAGE_NAME_2 = 'Data Validation Stage'
STAGE_NAME_3 = 'Data Transforamtion Stage'
try:
    logging.info(f"Stage {STAGE_NAME_1} started")
    data_ingestion = DataIngestionTrainPipeline()
    data_ingestion.main()
    logging.info(f"Stage {STAGE_NAME_1} completed")
    
    logging.info(f"Stage {STAGE_NAME_2} started")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logging.info(f"Stage {STAGE_NAME_2} completed")

    logging.info(f"Stage {STAGE_NAME_3} started")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logging.info(f"Stage {STAGE_NAME_3} completed")

except Exception as e:
    raise CustomException(e, sys)