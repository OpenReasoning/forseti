#!/usr/bin/env python
"""
setup routine
"""
from setuptools import setup, find_packages
import os


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as open_file:
        return open_file.read()

setup(
    # Metadata
    name='forseti',
    version='0.6.6',
    description='Formal Logic Framework',
    long_description=read('README.rst'),
    url='https://github.com/MasterOdin/forseti',
    download_url='https://pypi.python.org/pypi/forseti',
    license='MIT',
    author='Matthew Peveler',
    author_email='matt.peveler@gmail.com',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],

    # Dependencies
    tests_require=['nose', 'six'],

    # Contents
    packages=find_packages(exclude=['tests*']),

)
