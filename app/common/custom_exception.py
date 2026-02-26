import sys

class CustomException(Exception):
    def __init__(self, message, error_detail=None):
        self.error_message = self.get_detailed_error_message(message, error_detail)
        super().__init__(self.error_message)

    @staticmethod
    def get_detailed_error_message(message, error_detail=None):
        _, _, exc_tb = sys.exc_info()
        
        if exc_tb is not None:
            # Called inside an except block — full details available
            file_name = exc_tb.tb_frame.f_code.co_filename
            line_number = exc_tb.tb_lineno
            error_message = f"Error in file: {file_name} at line: {line_number} | {message} | Detail: {str(error_detail)}"
        else:
            # Called outside an except block — no traceback available
            error_message = f"Error: {message}"
            if error_detail:
                error_message += f" | Detail: {str(error_detail)}"
        
        return error_message

    def __str__(self):
        return self.error_message