"""
Module containing all file_organizer unit tests.
"""

import os
import shutil
import pytest
from file_organizer.config import Config
from file_organizer.file_handler import FileHandler
from file_organizer.logger import Logger
from file_organizer.regex_utils import get_file_type

@pytest.fixture
def setup_directories():
    # Setup source and destination directories for testing
    source_dir = 'test/test_source_directory'
    dest_dir = 'test/test_organized_files'
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(dest_dir, exist_ok=True)
    
    # Create test files
    open(os.path.join(source_dir, 'test_image.jpg'), 'a').close()
    open(os.path.join(source_dir, 'test_document.pdf'), 'a').close()
    open(os.path.join(source_dir, 'test_video.mp4'), 'a').close()
    open(os.path.join(source_dir, 'test_music.mp3'), 'a').close()
    open(os.path.join(source_dir, 'test_other.xyz'), 'a').close()

    yield source_dir, dest_dir

    # Cleanup after tests
    shutil.rmtree(source_dir)
    shutil.rmtree(dest_dir)

def test_config_loading():
    config = Config.load_config('file_organizer/config.json')
    assert 'source_directory' in config
    assert 'destination_directory' in config
    assert 'log_file' in config
    assert 'file_types' in config

def test_get_file_type():
    file_types = {
        'images': r'\.(jpg|jpeg|png|gif)$',
        'documents': r'\.(pdf|docx|txt)$',
        'videos': r'\.(mp4|mkv|avi)$',
        'music': r'\.(mp3|wav|flac)$',
        'archives': r'\.(zip|tar|gz|rar)$'
    }
    assert get_file_type('image.jpg', file_types) == 'images'
    assert get_file_type('document.pdf', file_types) == 'documents'
    assert get_file_type('video.mp4', file_types) == 'videos'
    assert get_file_type('music.mp3', file_types) == 'music'
    assert get_file_type('archive.zip', file_types) == 'archives'
    assert get_file_type('unknown.xyz', file_types) == 'others'

def test_file_handler(setup_directories):
    source_dir, dest_dir = setup_directories
    logger = Logger('test/test_log.log')
    file_types = {
        'images': r'\.(jpg|jpeg|png|gif)$',
        'documents': r'\.(pdf|docx|txt)$',
        'videos': r'\.(mp4|mkv|avi)$',
        'music': r'\.(mp3|wav|flac)$',
        'archives': r'\.(zip|tar|gz|rar)$'
    }
    file_handler = FileHandler(source_dir, dest_dir, file_types, logger)
    file_handler.organize_files()

    # Check if files are moved to the correct directories
    assert os.path.exists(os.path.join(dest_dir, 'images', 'test_image.jpg'))
    assert os.path.exists(os.path.join(dest_dir, 'documents', 'test_document.pdf'))
    assert os.path.exists(os.path.join(dest_dir, 'videos', 'test_video.mp4'))
    assert os.path.exists(os.path.join(dest_dir, 'music', 'test_music.mp3'))
    assert os.path.exists(os.path.join(dest_dir, 'others', 'test_other.xyz'))

def test_logger():
    log_file = os.path.abspath('test/test_log.log')
    logger = Logger(log_file)
    
    # Log a test message
    test_message = "This is a test log message."
    logger.log(test_message)
    
    # Log a test error
    test_error = "This is a test error message."
    logger.log_error(test_error)
    
    # Check if log file is created
    assert os.path.exists(log_file), f"Log file not found: {log_file}"
    
    # Check if log file contains the test message and error
    with open(log_file, 'r') as f:
        log_contents = f.read()
        assert test_message in log_contents, f"Test message not found in log file: {log_contents}"
        assert test_error in log_contents, f"Test error not found in log file: {log_contents}"

    # Clean up log file after test
    logger.close()
    os.remove(log_file)