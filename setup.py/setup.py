from setuptools import setup, find_packages

setup(
    name='binary_file_parser',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib'
    ],
    author='Tammie Koh',
    description='A package to parse and visualize the earthquake data for Linda.',
)