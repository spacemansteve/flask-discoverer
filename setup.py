#!/usr/bin/env python
"""
flask-discoverer
-------------

Flask extension that enables autodiscovery and broadcast of API endpoints
"""
from setuptools import setup


setup(
    name='flask-discoverer',
    version='0.0.1',
    url='http://github.com/adsabs/flask-discoverer/',
    license='MIT',
    author='Vladimir Sudilovsky',
    author_email='vsudilovsky@cfa.harvard.edu',
    description='Flask API autodiscovery',
    long_description=__doc__,
    py_modules=['flask_discoverer'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'flask-testing'
    ],
    test_suite='tests',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
