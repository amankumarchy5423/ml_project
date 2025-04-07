from src.exception.exception import project_exception
from src.logger.logger import my_logger
from dataclasses import dataclass
import os,sys



@dataclass
class data_ingestion_artifact:
    data_path : str
        

@dataclass
class data_validation_artifact:
            train_data_path : str
            test_data_path : str
        