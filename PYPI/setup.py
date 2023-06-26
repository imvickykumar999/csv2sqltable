from setuptools import setup

setup(
    name = 'csv2sqltable', # while installing pacakge
    version = '0.0.4',
    description = 'This package converts csv to sql table.',
    long_description = open('Readme.txt').read(),
    url = 'https://github.com/imvickykumar999',
    author = 'Vicky Kumar',
    keywords = ['csv to sql', 'table', 'database', 'magic sql', 'google colab'],
    license = 'MIT',
    packages = ['csv2sqltable'], # while importing package
    install_requires = ['']
)