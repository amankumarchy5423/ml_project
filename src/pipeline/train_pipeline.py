from src.component.data_ingestion import data_ingestion
from src.exception.exception import project_exception
from src.config.project_config import data_ingestion_config
from src.artifact.project_artifact import data_ingestion_artifact
from src.logger.logger import my_logger
import sys

class Trian_pipeline:
    def __init__(self):
        try:
            pass 
        except Exception as e:
            my_logger.error(f"Error in Trian_pipeline class: {str(e)}")
            project_exception(e,sys)
    
    def data_ingestion_pipeline(self):
        try:
            my_logger.info(">>>>> Data Ingestion Start <<<<<")
            data_ingestion_config_obj = data_ingestion_config()

            data_ingestion_artifact_obj = data_ingestion_artifact()

            data_ingestion_obj = data_ingestion(data_ingestion_config_obj,data_ingestion_artifact_obj)
            output = data_ingestion_obj.initiate_data_ingestion()
            my_logger.info(">>>>> Data Ingestion End <<<<<")
        except Exception as e:
            my_logger.error(f"Error in data_ingestion_pipeline method: {str(e)}")
            project_exception(e,sys)

