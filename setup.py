"""Pilot is a python library for traversing object trees and graphs
See:
https://github.com/tckerr/Pilot
https://pypi.python.org/pypi/pilot
"""

from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pilot',
    version='0.0.7',
    description='Pilot is a python library for traversing object trees and graphs',
    long_description=long_description,
    url='https://github.com/tckerr/Pilot',
    author='Tom Kerr',
    author_email='tckerr@gmail.com',
    liscence='GNU General Public License',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # until further tested
        'Programming Language :: Python :: 2.7',
    ],
    keywords='object development tree graph parse walk traverse data',
    packages=find_packages(),
    )