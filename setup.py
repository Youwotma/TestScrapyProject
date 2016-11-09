# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name         = 'project',
    version      = '1.0',
    packages     = find_packages(),
    scripts      = ['bin/hello.py'],
    entry_points = {'scrapy': ['settings = testscrapyproj.settings']},
)
