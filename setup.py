import os
from setuptools import setup

requires=[
    'wheel',
    'pillow',
]


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()

setup(
    name='pixelate',
    version='1.0',
    author='Georgy Bazhukov',
    author_email='georgy.bazhukov@gmail.com',
    url='https://github.com/useless-tools/pixelate',
    
    description='The library / CLI-utility provides pixelation of images',
    long_description=read('README.rst'),
    packages=('pixelate',),
    py_modules=('pixelate',),
    include_package_data=True,
    
    license="BSD",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    
    requires=requires,
    tests_require=requires + ["pytest"],
    setup_requires=requires + ["pytest-runner"],
    install_requires=requires,
    
    scripts=['bin/pixelate'],
)
