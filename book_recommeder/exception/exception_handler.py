import os
import sys

class AppException(Exception):
    def __innit__(self,error_message: Exception,error_detail: sys):
        super().__innit__(error_message)
        self.error_message = AppException.error_message_detail(error_message,error_detail=error_detail)

@staticmethod
def error_messege_detail(error:Exception, error_detail: sys):
    

    _,_, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename


    error_messege = f"Error Occured python scriptname [{file_name}]"\
                    f" line number [{exc_tb.tb_lineno}] error messege [{error}]"
    
    return error_messege


def __repr__(self):
    return AppException.__name__.__str__()


def __str__(self):
    return self.error_message
    

    
                     