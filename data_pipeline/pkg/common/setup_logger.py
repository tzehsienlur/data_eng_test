import logging
import time
import os
from logging.handlers import RotatingFileHandler

# Constants
from pkg.common.common_config import LOG_FILE_NAME, MAX_BYTES, TOTAL_LOGFILES


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Make director if log folder does not exist
if not os.path.exists(LOG_FILE_NAME):
    os.mkdir(LOG_FILE_NAME)
    print("Directory " , LOG_FILE_NAME ,  " Created ")

# Create a rotating logger whereby when file reaches 10MB create a new log file
# up to 10 files can be created, if exceed limit replace the oldest file
handler = RotatingFileHandler(LOG_FILE_NAME + "/data_pipeline.log", maxBytes=MAX_BYTES, backupCount=TOTAL_LOGFILES)

formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)