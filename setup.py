"""Pilot is a python library for traversing object trees and graphs
See:
https://github.com/tckerr/Pilot
"""

from setuptools import setup, find_packages

setup(
    name='pilot',
    version='0.0.1',
    description='Pilot is a python library for traversing object trees and graphs',
    long_description='Pilot is a python library that allows for injecting callback hooks into tree/graph traversal, as well as for providing metadata about traversed nodes and their relationships.',
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