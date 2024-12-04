"""
Custom error handling for file organizer.
"""

class FileOrganizerError(Exception):
    pass

class FileNotFoundError(FileOrganizerError):
    pass

class PermissionError(FileOrganizerError):
    pass