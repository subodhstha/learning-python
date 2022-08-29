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

