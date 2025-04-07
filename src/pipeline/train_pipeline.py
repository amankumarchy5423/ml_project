from src.component.data_ingestion import data_ingestion
from src.exception.exception import project_exception
from src.config.project_config import data_ingestion_config
from src.artifact.project_artifact import data_ingestion_artifact

from src.config.project_config import data_validation_config
from src.artifact.project_artifact import data_validation_artifact
from src.component.data_validation import data_validation

from src.logger.logger import my_logger
import sys

class Trian_pipeline:
    def __init__(self):
        try:
            pass
        except Exception as e:
            my_logger.error(f"Error in Trian_pipeline class: {str(e)}")
            project_exception(e,sys)
    
    def data_ingestion_pipeline(self) -> data_ingestion_artifact:
        try:
            my_logger.info(">>>>> Data Ingestion Start <<<<<")
            data_ingestion_config_obj = data_ingestion_config()

            # data_ingestion_artifact_obj = data_ingestion_artifact()

            data_ingestion_obj = data_ingestion(data_ingestion_config_obj)
            output = data_ingestion_obj.initiate_data_ingestion()

            return output
            my_logger.info(">>>>> Data Ingestion End <<<<<")
        except Exception as e:
            my_logger.error(f"Error in data_ingestion_pipeline method: {str(e)}")
            project_exception(e,sys)

    
    def data_validation_pipeline(self,ingestion_artifact) -> data_validation_artifact:
        try:
            my_logger.info(">>>> data validation start <<<<<")
            data_validation_config_obj = data_validation_config()
            my_logger.info("data validation config object created")

    
            data_validation_obj = data_validation(validation_config=data_validation_config_obj,
                                                  ingestion_artifact=ingestion_artifact)
            my_logger.info("data validation object created")
            
            output  = data_validation_obj.initiate_data_validation()
            my_logger.info("data validation completed")
            
            my_logger.info(">>>> data validation end  <<<<<")
        except Exception as e:
            my_logger.error(f"Error in data_validation_pipeline method: {str(e)}")
            project_exception(e,sys)

    def initiate_train_pipeline(self):
        try:
            my_logger.info(">>>>> Train Pipeline Start <<<<<")
            data_ingestion_out = self.data_ingestion_pipeline()

            data_validation_out = self.data_validation_pipeline(data_ingestion_out)
        
        except Exception as e:
            my_logger.error(f"Error in initiate_train_pipeline method: {str(e)}")
            project_exception(e,sys)

