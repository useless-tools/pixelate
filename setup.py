#!/usr/bin/env python
# coding: utf-8

import sys
from setuptools import setup, find_packages

requires=[
    'pillow',
]

setup(
    name='pixelate',
    version='0.4',
    author='Georgy Bazhukov',
    author_email='georgy.bazhukov@gmail.com',
    description='Library provides pixelation for images',
    long_description="""
# pixelate

Make your photos worse. But it looks like pixel art.

Works with Python >= 2.6, Python >= 3.2.

## Installation

    pip install pixelate

## Example

    pixelate --input=img/bps.jpg --output=img/bps.png --pixel-size=10

see more https://github.com/useless-tools/pixelate
""",
    url='https://github.com/useless-tools/pixelate',
    packages=find_packages(),
    include_package_data=True,
    license="BSD",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite="runtests",
    requires=requires,
    tests_require=requires,
    setup_requires=requires,
    scripts=['bin/pixelate'],
)
