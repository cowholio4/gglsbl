#!/usr/bin/env python2.7

from setuptools import setup
import versioneer

import sys, os

setup(name='gglsbl',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Client library for Google Safe Browsing API",
    classifiers=[
        "Operating System :: POSIX",
        "Environment :: Console",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='safe browsing api client',
    author='Aleh Filipovich',
    author_email='aleh@vaolix.com',
    url='https://github.com/afilipovich/gglsbl',
    license='Apache2',
    packages=['gglsbl'],
    install_requires=['argparse', 'pysqlite', 'googleapiclient', 'versioneer'],
    scripts=['bin/gglsbl_client.py'],
)
