from src.component.data_ingestion import data_ingestion
from src.pipeline.train_pipeline import Trian_pipeline
from src.logger.logger import my_logger



if __name__  == '__main__':
    # data ingestion
   print("project start")
   my_logger.info(">>>>> Taining Pipeline start <<<<<")
   obj_train_pipeline = Trian_pipeline()
   obj_train_pipeline.initiate_train_pipeline()
   my_logger.info(">>>>> Taining Pipeline ended <<<<<")
   print("project ended")

