# import logging
# logging.debug("This is a debug message")
# logging.info("This is a an info message")
# logging.warning("This is a warning message")
# logging.error("This is error message")
# logging.critical("This is a critical message")


# import logging
# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%m/%d/%Y %H:%M%S")
# logging.debug("This is a debug message")
# logging.info("This is a an info message")
# logging.warning("This is a warning message")
# logging.error("This is error message")
# logging.critical("This is a critical message")


# import logging
# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%m/%d/%Y %H:%M%S")
# import helper



# import logging

# logger = logging.getLogger(__name__)

# # create handler
# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler("./intermediate/file.log")

# # level and the format
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning("This is a warning")
# logger.error("This is an error")



# import logging
# import logging.config

# logging.config.fileConfig("logging.conf")

# logger = logging.getLogger("simpleExample")
# logger.debug("This is a debug message")


# import logging
# import traceback
# try:
#     a = [1, 2, 3]
#     val = a[4]
# except:
#     logging.error("The error is %s", traceback.format_exc())

# # except IndexError as e:
# #     logging.error(e, exc_info= True)



# import logging
# from logging.handlers import RotatingFileHandler

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# # roll over after 2KB, and keep backup logs app.log.1, app.log.2 , etc.
# handler = RotatingFileHandler("intermediate/app.log", maxBytes= 2000, backupCount=5)
# logger.addHandler(handler)

# for _ in range(10000):
#     logger.info("Hello world")

import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# s, m, h, d, midnight, w0(monday), w1(tuesday) ...
handler = TimedRotatingFileHandler("intermediate/Timed_test.log", when = "s", interval = 5, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info("Hello world")
    time.sleep(5)