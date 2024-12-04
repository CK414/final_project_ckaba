"""
Handles logging of operations.
"""

import logging
import os

class Logger:
    def __init__(self, log_file):
        log_file = os.path.abspath(log_file)
        log_dir = os.path.dirname(log_file)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)    
        print(f"Creating log file at: {log_file}")  # Debug statement
        
        # Clear any existing handlers
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filemode='w'
        )
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.handler = logging.FileHandler(log_file, mode='w')
        self.handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(self.handler)

    def log(self, message):
        # print(f"Logging message: {message}")  # Debug statement
        self.logger.info(message)
        self.handler.flush()

    def log_error(self, error):
        print(f"Logging error: {error}")  # Debug statement
        self.logger.error(error)
        self.handler.flush()
        
    def close(self):
        print("Closing log handler")  # Debug statement
        self.logger.removeHandler(self.handler)
        self.handler.close()
        logging.shutdown()