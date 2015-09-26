#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup

REQUIRES = [
    'pyquery',
    'docopt',
]

INSTALL_REQUIRES=[
    'pyquery',
    'docopt',
]

setup(name='pquery',
      version='1.4',
      description='grep for HTML; CLI for pyquery',
      author='Pili Hu',
      author_email='me@hupili.net',
      maintainer='Pili Hu',
      maintainer_email='me@hupili.net',
      url='https://github.com/hupili/pquery',
      scripts=['pquery'],
      provides=['pquery'],
      requires=REQUIRES,
      install_requires=INSTALL_REQUIRES,
      classifiers=[
          'License :: Public Domain',
          'Intended Audience :: Developers',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Science/Research',
          'Natural Language :: English',
          'Programming Language :: Python :: 2.7',
          'Development Status :: 4 - Beta',
          'Topic :: Internet',
      ]
     )
