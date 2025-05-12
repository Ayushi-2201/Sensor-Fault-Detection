import sys
# This module gives you access to system-level functions and objects.
# In this code, it's used to **get detailed information** about the exception (like filename and line number).
# It also gives exact details about the exception which is not possible for os module which could only be used for filename and line number.

def error_message_detail(error, error_detail: sys):
    """
    This function takes an error and its details from sys and returns a formatted error message.

    error - hold the actual exception object, 
            gets its value when an exception occurs and is passed in (as e in except Exception as e:)
            Example: if an error happens due to 1/0, this error becomes something like ZeroDivisionError('division by zero').

    error_detail - holds the details of the exception,
                    pass the sys module itself into the function so it can access sys.exc_info().

    : sys - is just a type hint.



    """
    _, _, exc_tb = error_detail.exc_info()
    """
    _, _, - they are variables that we don't need to use, so we use _ to ignore them.

    error_details - is basically same as sys, or we can access the sys module using error_detail variable.

    exc_info() = a function that returns 3 things:

        The exception type (like ZeroDivisionError)

        The exception instance (like ZeroDivisionError('division by zero'))

        The traceback object (tells you where the error occurred)
    """

    file_name = exc_tb.tb_frame.f_code.co_filename
    """
    Traceback object (exc_tb) holds:

        tb_frame = the actual stack frame where the error occurred.

        f_code = the code object.

        co_filename = the filename of the Python file.

    This gives us: Which file had the error.


    """

    line_number = exc_tb.tb_lineno
    """
    tb_lineno tells us the line number where the exception occurred.
    """

    error_message = f"Error occurred in python script: [{file_name}] at line number: [{line_number}] error message: [{str(error)}]"

    """
    str(error) - The error message itself (e.g., "division by zero")
    """
    return error_message


class CustomException(Exception):
    def __init__(self, error_message: str, error_detail: sys):
        """
        error_message: the raw string version of the error (like "division by zero")
        error_detail: the sys module, again used for exc_info()
        """
        super().__init__(error_message)
        """
        It’s doing two things:

            Calling the parent class’s __init__() method — this ensures that your custom exception gets set up like a normal exception.

            Passing error_message to that parent method — so that the parent Exception class can store the message you provided.
        """
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )
        """
        
        """

    def __str__(self):
        """
        __str__ - Customizes how the object appears when printed or converted to a string.
        """

        """
        Whenever someone tries to convert this exception object to a string (like printing it), just return the value of self.error_message.
        """
        return self.error_message
