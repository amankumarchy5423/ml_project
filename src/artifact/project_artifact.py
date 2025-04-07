from src.exception.exception import project_exception
from src.logger.logger import my_logger
from dataclasses import dataclass
import os,sys



# @dataclass
class data_ingestion_artifact:
    """Data Ingestion Artifact Class"""

    def __init__(self):
        try :
            data_path : str
        except Exception as e:
            my_logger.error(f"Error in data_ingestion_artifact class: {str(e)}")
            raise project_exception(e,sys)

    


