'''
file_organizer init module also containing the main module.
'''
import json
from .file_handler import FileHandler
from .logger import Logger
from .config import Config

def main():
    print("Loading configuration...")
    config = Config.load_config()
    formatted_config = json.dumps(config, indent=4)
    print("Configuration loaded:")
    print(formatted_config)  # Pretty-print the configuration
    
    logger = Logger(config['log_file'])
    logger.log("Configuration loaded:")
    logger.log(formatted_config)
    file_handler = FileHandler(config['source_directory'], config['destination_directory'], config['file_types'], logger)
    
    try:
        print("Starting file organization...")
        file_handler.organize_files()
        print("File organization completed.")
    except Exception as e:
        logger.log_error(e)
        print(f"An error occurred: {e}")
    finally:
        logger.close()
