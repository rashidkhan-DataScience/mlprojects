
#%%
import sys
import warnings

warnings.filterwarnings('ignore')

def error_message_detail(error,error_detail:sys):

    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_num = exc_tb.tb_frame.f_lineno

    error_message = f"Error occured in python script name {file_name} line number {exc_tb.tb_lineno} error message {str(error)}"

    return error_message

class CustomExceptio(Exception):

    def __init__(self, error, error_detail:sys):
        super().__init__(error)
        self.error_message = error_message_detail(error,error_detail)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":

    try:
        1/0
    except Exception as e:
        print(e)
        print('-'*36)
        raise CustomExceptio(e,sys)