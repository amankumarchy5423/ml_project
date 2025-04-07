import exception
import sys
import os
# from src.logger.logger import my_logger




# class project_exception(Exception):
#     def __init__(self,erreo_info,error_details : sys):
#         try:
            
#             _,_,exc_tb = error_details.exc_info()
#             self.line_number = exc_tb.tb_lineno
#             self.error_message = f"{erreo_info} with error details: {error_details}"
#             self.file_name  = exc_tb.tb_frame.f_code.co_filename
#         except Exception as e:
#             print(f"An error occurred: {e}")

#     def __str__(self):
#         return f"{self.error_message}(file : {self.file_name}),(line : {self.line_number})"
    
class project_exception(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()
        
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename 
    
    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))
    
if __name__=='__main__':
    try:
        # my_logger.info("Enter the try block")
        a=1/0
        print("This will not be printed",a)
    except Exception as e:
        # my_logger.error(e)
        raise project_exception(e,sys)
        

