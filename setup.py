#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
import sys

base_path = '%s/etc/' % os.getenv('VIRTUAL_ENV', '')
data_files = dict()
data_files[base_path] = ['postapi_api.conf']

console_scripts = ['postapi_api=postapi_api.main:app']
install_requires = ['redis>=2.10.6']
tests_require = []
extras_require = {}

setup(name='postapi_api',
      version='1.0.0',
      description='A postfix API to handle reply addresses',
      url='https://github.com/jondkelley/postapi-api/',
      packages=find_packages(),
      author='Jon Kelley',
      author_email='jonkelley@gmail.com',
      license='BSD',
      entry_points={'console_scripts': console_scripts},
      data_files=[(key, data_files[key]) for key in data_files.keys()],
      install_requires=install_requires,
      extras_require=extras_require,
      tests_require=tests_require,
      classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: BSD License',
            'Operating System :: POSIX',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Topic :: System :: Monitoring'])
