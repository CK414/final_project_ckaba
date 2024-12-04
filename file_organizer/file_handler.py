"""
Handles file organization based on file types.
"""

import os
import shutil
from .regex_utils import get_file_type

class FileHandler:
    def __init__(self, source_directory, destination_directory, file_types, logger):
        self.source_directory = source_directory
        self.destination_directory = destination_directory
        self.file_types = file_types
        self.logger = logger

    def organize_files(self):
        if not os.path.exists(self.source_directory):
            raise FileNotFoundError(f"Source directory '{self.source_directory}' does not exist.")
        
        if not os.path.exists(self.destination_directory):
            os.makedirs(self.destination_directory, exist_ok=True)
        
        for root, _, files in os.walk(self.source_directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_type = get_file_type(file, self.file_types)
                dest_folder = os.path.join(self.destination_directory, file_type)
                os.makedirs(dest_folder, exist_ok=True)
                dest_path = os.path.join(dest_folder, file)
                shutil.move(file_path, dest_path)
                normalized_dest_path = os.path.normpath(dest_path)
                self.logger.log(f"Moved {file} to {normalized_dest_path}")
                print(f"Moved {file} to {normalized_dest_path}")