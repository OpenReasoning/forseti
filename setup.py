#!/usr/bin/env python
"""
setup routine
"""
from setuptools import setup, find_packages
import os
from pip.req import parse_requirements


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as open_file:
        return open_file.read()


def get_requirements():
    """Get requirements from requirements.txt file"""
    install_reqs = parse_requirements("requirements.txt")
    return [str(ir.req) for ir in install_reqs[1:]]

setup(
    # Metadata
    name='Forseti',
    version='0.5.0',
    description='Formal Logic Framework',
    long_description=read('README.md'),
    url='https://github.com/MasterOdin/Forseti',
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
    install_require=['pip'],
    tests_require=get_requirements(),

    # Contents
    packages=find_packages(exclude=['tests*']),

)
