import sys
from textSummarizer.components.data_transformation import DataTransformation
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.exceptions import CustomException

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_transformation_config()
            data_validation = DataTransformation(config=data_validation_config)
            data_validation.convert()
        except Exception as e:
            raise CustomException(e, sys)