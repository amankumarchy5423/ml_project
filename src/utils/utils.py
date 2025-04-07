import os
import sys
from src.exception.exception import project_exception
# from src.logger.logger import my_logger



def create_dir(file_path):
    try:
        
        os.makedirs(os.path.dirname(file_path),exist_ok=True)

    except Exception as e:
        # my_logger.error(f"Error creating directory: {str(e)}")
        project_exception(e,sys)