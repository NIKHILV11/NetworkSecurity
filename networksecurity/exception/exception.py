import sys
from networksecurity.logging import logger
class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_details : sys):
        self.error_message = error_message
        _, _, tb = error_details.exc_info()
        self.lineno = tb.tb_lineno
        self.filename = tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error: {self.error_message} at line {self.lineno} in {self.filename}"

