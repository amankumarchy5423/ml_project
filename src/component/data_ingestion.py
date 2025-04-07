from src.exception.exception import project_exception
from src.logger.logger import my_logger
from src.attribute import project_attribute 
from src.config.project_config import data_ingestion_config
from src.utils.utils import create_dir
from src.artifact.project_artifact import data_ingestion_artifact

import os
import sys
import pymongo
import pandas as pd 
import numpy as np
import json

from dotenv import load_dotenv
load_dotenv()
url = os.getenv('MONGO_URI')

import certifi
ca =  certifi.where()




class data_ingestion:
        def __init__(self,config : data_ingestion_config,
                     artifact : data_ingestion_artifact):
            try:
                 self.config = config
                 self.artifact = artifact
            except Exception as e :
                my_logger.info(e)
                project_exception(e,sys)

        def mongo_connection(self,uri:str ):
             try:
                  client = pymongo.MongoClient(uri,tlsCAFile = ca)
                  db = client[self.config.database][self.config.collection]
                  my_logger.info("mongo client are connected ....")

                  data = db.find()
                  my_logger.info("data founded ....")

                  lis_data = list(data)
                  my_logger.info("now converting data to list because mongo atlas return Cursor type object ....")

                  df = pd.DataFrame(lis_data)
                  my_logger.info("data are converted to pandas data frame ....")

                  print(f"type of data is {df.head(2)}")

                  return df
             except Exception as e:
                  my_logger.info(e)
                  project_exception(e,sys)
                  raise e

        def data_fetching(self,file_dir,data):
             try:
                  create_dir(file_path=file_dir)
                  
                  my_logger.info("directory created ....")
                  file_name = os.path.dirname(file_dir)

                  data.to_csv(file_dir,index = False)
               #    with open(file_dir, 'w') as f:
               #         for item in data:
               #              f.write("%s\n" % item)
                  my_logger.info(f"data sample {file_dir}")
                  return file_dir
             except Exception as e:
                  my_logger.info(e)
                  project_exception(e,sys)
                  raise e


        def initiate_data_ingestion(self):
             try:
                  data_file_path = self.config.data_file_path

                  my_logger.info("now start mongo_connection ...")
                  data = self.mongo_connection(uri=url)

                  my_logger.info("now start data fetching ...")
                  file = self.data_fetching(data=data,file_dir=data_file_path)

                  my_logger.info("creating data ingestion artifact object  ....")
                  data_artifact = self.artifact(data_path=file)

                  return data_artifact

             

                  my_logger.info("all data_ingestion process completed ....")
             except Exception as e:
                  my_logger.info(e)
                  project_exception(e,sys)
                  raise e
    
        
