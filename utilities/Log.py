import inspect
import logging
import sys


def log():
    logger = logging.getLogger(inspect.stack()[1][3])

    fileHandler = logging.FileHandler('logfile.log')
    fileHandler.setLevel(logging.INFO)

    streamHandler = logging.StreamHandler(sys.stdout)
    streamHandler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

    fileHandler.setFormatter(formatter)
    streamHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # pass filehandler object
    logger.addHandler(streamHandler)

    logger.setLevel(logging.INFO)

    return logger
