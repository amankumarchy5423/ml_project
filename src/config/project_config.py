from src.exception.exception import project_exception
from src.logger.logger import my_logger
from src.attribute import project_attribute 


import os
import sys
from dotenv import load_dotenv
load_dotenv()

uri = os.getenv('MONGO_URI')
# print("MongoDB URI:", mogo_uri)

class data_ingestion_config:
    def __init__(self):
        try:
            self.mongo_uri = uri
            self.database :str = project_attribute.MONOGO_DATABASE
            self.collection = project_attribute.MONO_COLLECTION
            self.data_file_path = os.path.join(
                project_attribute.DATA_INGESTION_DIR,
                project_attribute.DATA_INGESTION_FILE
            )
        except Exception as e :
            my_logger.error(f"Error in project_config: {str(e)}")
            project_exception(e,sys)

class data_validation_config:
    def __init__(self):
        try:
            self.vaidation_dir : str = project_attribute.DATA_VALIDATION_DIR
            self.validation_test_file : str = os.path.join(self.vaidation_dir,project_attribute.TEST_FILE)
            self.validation_train_file : str = os.path.join(self.vaidation_dir,project_attribute.TRAIN_FILE)
            self.missing_value_threshold : float  = 0.6
        except Exception as e :
            my_logger.error(f"Error in project_config: {str(e)}")
            project_exception(e,sys)