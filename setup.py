"""
Allows you to install the package using setuptools
"""

from setuptools import setup, find_packages

setup(
    name="FinalProjectCKaba",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "geopy", # For calculating distances
        "networkx", # For making graph nodes and edges
        "matplotlib", # For plotting graphs
        'pytest',  # For running tests
        'logging',  # For logging operations
    ],
    entry_points={
        "console_scripts": [
            # Allows the main function of TarjanPlanner to be run by typing
            # 'TarjanPlanner' in the console
            "TarjanPlanner=tarjan_planner:main",
            # Allows the main function of FileOrganizer to be run by typing
            # 'FileOrganizer' in the console
            "FileOrganizer=file_organizer:main",
        ]
    },
)
