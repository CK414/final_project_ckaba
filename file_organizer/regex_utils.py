"""
Utility functions for regular expressions.
"""

import re

def get_file_type(file_name, file_types):
    for file_type, pattern in file_types.items():
        if re.search(pattern, file_name, re.IGNORECASE):
            return file_type
    return 'others'