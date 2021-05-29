# -*- coding: utf-8 -*-

import os
from setuptools import setup

os.system("cd stringcheese/pyahocorasick-1.4.0/; python setup.py install")

setup(
    name         = 'stringcheese',
    version      = '1.0',
    description  = '',
    url          = 'https://github.com/MathisHammel/stringcheese',
    author       = 'Mathis Hammel',
    author_email = 'e@e.e',
    license      = 'GPL2',
    packages     = ['stringcheese'],
    zip_safe     = False
)



