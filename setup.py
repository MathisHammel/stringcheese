# -*- coding: utf-8 -*-

import os
import setuptools
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
os.system("cd stringcheese/pyahocorasick-1.4.0/; python setup.py install")

setuptools.setup(
    name         = 'stringcheese',
    version      = '1.1',
    description  = 'StringCheese is a tool to get easy CTF flags automatically.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url          = 'https://github.com/MathisHammel/stringcheese',
    author       = 'MathisHammel',
    author_email = 'mathis@h25.io',
    license      = 'GPL2',
    packages     = ['stringcheese'],
    entry_points = {
        'console_scripts' : ['stringcheese=stringcheese.__main__:main']
    },
    install_requires = [
        'tqdm'
    ],
    zip_safe     = False
)

