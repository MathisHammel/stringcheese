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
    extras_require = { 'build': ['tqdm'] },
    zip_safe     = False
)

f = open('/bin/stringcheese','w')
f.write('#!/bin/bash\npython3 -m stringcheese ${@}\n')
f.close()
os.system("chmod +x /bin/stringcheese")
