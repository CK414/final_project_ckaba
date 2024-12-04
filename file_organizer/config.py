"""
Handles configuration loading.
"""

import json

class Config:
    @staticmethod
    def load_config(config_file='file_organizer/config.json'):
        with open(config_file, 'r') as file:
            return json.load(file)