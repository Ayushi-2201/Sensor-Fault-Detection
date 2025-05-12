import logging
import os       # provides functionality of reading and writing files in the file system
from datetime import datetime 

LOG_FILE = f"{datetime.now().strftime("%Y-%m-%d-%H-%M-%s")}.log"    # generates a log file name with the current date and time

logs_path=os.path.join(os.getcwd(), "logs")   # creates a path for the log file in the logs directory
# os.path.join Use the join function from the path submodule of the os module.
# os.getcwd()	Returns the current working directory
# "logs"	A subdirectory (We want to go into a folder named logs).

os.makedirs(os.path.dirname(logs_path), exist_ok=True)  # creates the logs directory if it doesn't exist
# os.makedirs()	Recursively create directories.

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)  # creates the full path for the log file

logging.basicConfig(
    filename=LOG_FILE_PATH,  # sets the log file path
    level=logging.INFO,  # sets the logging level to DEBUG
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)",  # sets the log message format
)
