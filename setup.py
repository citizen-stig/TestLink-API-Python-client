#! /usr/bin/python
# -*- coding: UTF-8 -*-

#  Copyright 2012-2013 Luiko Czub, TestLink-API-Python-client developers
#
#  Licensed under Apache 2.0 
#  

from os.path import join, dirname
from distutils.core import setup

execfile(join(dirname(__file__), 'src', 'testlink', 'version.py'))

setup(name='TestLink',
      version=VERSION,
      description='Python XMLRPC client for the TestLink API',
      author='James Stock, Olivier Renault, Luiko Czub, TestLink-API-Python-client developers',
      author_email='orenault@gmail.com, Luiko.Czub@Liegkat-Archiv.de',
      url='https://github.com/lczub/TestLink-API-Python-client',
      license      = 'Apache 2.0',
      package_dir  = {'': 'src'},
      packages=['testlink'],
     )

