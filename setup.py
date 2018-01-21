#!/usr/bin/env python

from setuptools import setup

setup(
    name='face',
    version='0.1',
    packages=['face'],
    include_package_data=True,
    install_requires=[
        'flask',
    ]
)
