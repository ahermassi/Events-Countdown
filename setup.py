#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


NAME = 'events-countdown'
DESCRIPTION = 'CLI tool to count days remaining until events.'
URL = 'https://github.com/ahermassi/Events-Countdown'
EMAIL = 'hermassi.anouer@gmail.com'
AUTHOR = 'Anouer Hermassi'
REQUIRES_PYTHON = '>=3.6.0'
REQUIRED = [
    'colorama', 'pyyaml', 'click'
]

setup(
    name=NAME,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=['events_countdown'],
    entry_points={
        'console_scripts': 'events-countdown=events_countdown.main:main'
    },
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT'
)
