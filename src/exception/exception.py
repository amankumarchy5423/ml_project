import exception
import sys
import os




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
    def __init__(self, error_info, error_details: sys):
        try:
            _, _, exc_tb = error_details.exc_info()
            self.line_number = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename
            self.error_message = f"{error_info} | File: {self.file_name}, Line: {self.line_number}"
        except Exception as e:
            self.error_message = f"Failed to extract error details: {e}"
            self.line_number = None
            self.file_name = None

    def __str__(self):
        return self.error_message

