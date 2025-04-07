import pandas as pd
import numpy as np
import os
import sys
from sklearn.model_selection import train_test_split
from src.exception.exception import project_exception
from src.logger.logger import my_logger
from src.artifact.project_artifact import data_validation_artifact
from src.config.project_config import data_validation_config
from src.artifact.project_artifact import data_ingestion_artifact

data = pd.read_csv("network_data/data/data.csv")
print(data.head())


class data_validation :
    def __init__(self,validation_config : data_validation_config,
                 ingestion_artifact ):
        try:
            # self.artifact = validation_artifact
            self.config = validation_config
            self.ingestion_artifact = ingestion_artifact
        except Exception as e:
            my_logger.error(f"Error Occured : {e}")
            project_exception(e,sys)

    def data_drift(self,data):
        try:
            # Check for missing values
            drift_repo = True
            if self.config.missing_value_threshold > 0:
                missing_value_count = data.isnull().sum()
                if missing_value_count.max() > self.config.missing_value_threshold:
                    drift_repo = False

                    my_logger.error(f'''Data Drift: Missing values detected. Maximum missing value count is 
                                    {missing_value_count.max()}. Threshold is {self.config.missing_value_threshold}''')
                    project_exception("Data Drift: Missing values detected", sys)
        except Exception as e:
            my_logger.error(f"Error Occured : {e}")
            project_exception(e, sys)

    def data_to_train_test(self,data):
        try:
            train_data,test_data = train_test_split(data,train_size=0.8)
            my_logger.info("data is divided in train and test part")

            os.makedirs(self.config.vaidation_dir,exist_ok=True)
            my_logger.info("validation directory created ")

            train_data.to_csv(self.config.validation_train_file)
            test_data.to_csv(self.config.validation_test_file)
            my_logger.info("validation train and test file created and data saved ")

        except Exception as e:
            my_logger.error(f"Error Occured : {e}")
            project_exception(e, sys)
    
    def initiate_data_validation(self):
        try:
            data = pd.read_csv(self.ingestion_artifact.data_path)
            my_logger.info("data read from the directory")

            report = self.data_drift(data)
            my_logger.info("data drift check done")

            self.data_to_train_test(data)
        except Exception as e:
            my_logger.error(f"Error Occured : {e}")
            project_exception(e, sys)


            
                    
                # Check for duplicate values

