"""
Module containing all logging functions.
"""

import logging
import os
import time


def setup_logger():
    """
    Sets up the logger for the application.
    """
    logger = logging.getLogger("tarjan_planner_logger")
    logger.setLevel(logging.DEBUG)

    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler("tarjan_planner/tarjan_planner.log")
    c_handler.setLevel(logging.INFO)
    f_handler.setLevel(logging.DEBUG)

    # Create formatters and add them to handlers
    c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger


# Initialize the logger
logger = setup_logger()


def clear_log_file():
    """
    Clears all data in the logger file.
    """
    log_file_path = "tarjan_planner/tarjan_planner.log"

    # Clear the log file
    with open(log_file_path, "w"):
        pass

    logger.info("Log file cleared.")


# Decorator for logging execution time
def log_execution_time(func):
    """
    Decorator to log the execution time of a function.
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logger.info(f"Executed {func.__name__} in {execution_time:.4f} seconds")
        return result

    return wrapper
