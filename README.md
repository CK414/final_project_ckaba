# ACIT4420 Final Project - Tarjan Planner & File Organizer
 Final Project for ACIT 4420

This project contains two modules: Tarjan Planner and File Organizer.

## Features

- **Tarjan Planner**: A module for planning the most efficient path for Tarjan to take through Seoul, S. Korea while delivering gifts to his relatives.
- **File Organizer**: A module to organize files in a directory based on their file types.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/CK414/final_project_ckaba.git
    cd final_project_ckaba
    ```

2. **Build and install the package locally:**

    ```sh
    python setup.py sdist bdist_wheel
    pip install dist/final_project_ckaba-1.0.0-py3-none-any.whl
    ```

## Running the Modules

### File Organizer

1. **Ensure the source directory contains files to be organized.**

2. **Run the File Organizer module:**

    ```sh
    FileOrganizer
    ```

### Tarjan Planner

1. **Run the Tarjan Planner module:**

    ```sh
    TarjanPlanner
    ```

## File Organizer Configuration

The configuration file `config.json` for the File Organizer module contains settings for the source directory, destination directory, log file, and file type patterns. You can customize these settings as needed.

Example `config.json`:

```json
{
    "source_directory": "file_organizer/source_directory",
    "destination_directory": "file_organizer/organized_files",
    "log_file": "file_organizer/file_organizer.log",
    "file_types": {
        "images": "\\.(jpg|jpeg|png|gif)$",
        "documents": "\\.(pdf|docx|txt)$",
        "videos": "\\.(mp4|mkv|avi)$",
        "music": "\\.(mp3|wav|flac)$",
        "archives": "\\.(zip|tar|gz|rar)$"
    }
}
