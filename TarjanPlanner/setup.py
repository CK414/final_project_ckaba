from setuptools import setup, find_packages

setup(
    name="TarjanPlanner",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'geopy',
        'networkx',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': [
            # Allows the main function of module to be run by typing 'python TarjanPlanner' in the console
            'TarjanPlanner=TarjanPlanner.main:main'
        ]
    }
)