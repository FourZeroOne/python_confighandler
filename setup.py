from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='python_confighandler',
    version='0.1.0',
    description='Python Confighandler',
    long_description=long_description,
    author='Johannes Eimer',
    author_email='info@jep-dev.com',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[],
    python_requires='>=3.6',
    url="https://github.com/FourZeroOne/python_confighandler"
)
