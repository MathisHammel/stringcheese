# -*- coding: utf-8 -*-

import os
import setuptools
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info
from os import path

## Checking Python version == 3.*
from sys import version_info as python_version

if python_version.major not in [3]:
    raise ValueError('Python %s is not supported' % python_version)

## Reading long_description
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

## Install pyahocorasick
pyahocorasick_dir = "./stringcheese/pyahocorasick-1.4.0/"

module = setuptools.Extension(
    'stringcheese.ahocorasick',
    sources=[
        pyahocorasick_dir+'pyahocorasick.c',
    ],
    define_macros=[], #[('AHOCORASICK_UNICODE', '')],
    depends=[pyahocorasick_dir+d for d in [
        'common.h',
        'Automaton.c',
        'Automaton.h',
        'Automaton_pickle.c',
        'AutomatonItemsIter.c',
        'AutomatonItemsIter.h',
        'AutomatonSearchIter.c',
        'AutomatonSearchIter.h',
        'AutomatonSearchIterLong.c',
        'AutomatonSearchIterLong.h',
        'trie.c',
        'trie.h',
        'slist.c',
        'utils.c',
        'trienode.c',
        'trienode.h',
        'msinttypes/stdint.h',
        'src/inline_doc.h',
        'src/pickle/pickle.h',
        'src/pickle/pickle_data.h',
        'src/pickle/pickle_data.c',
        'src/custompickle/custompickle.h',
        'src/custompickle/custompickle.c',
        'src/custompickle/pyhelpers.h',
        'src/custompickle/pyhelpers.c',
        'src/custompickle/save/automaton_save.h',
        'src/custompickle/save/automaton_save.c',
        'src/custompickle/save/savebuffer.h',
        'src/custompickle/save/savebuffer.c',
        'src/custompickle/load/module_automaton_load.h',
        'src/custompickle/load/module_automaton_load.c',
        'src/custompickle/load/loadbuffer.h',
        'src/custompickle/load/loadbuffer.c',
        'src/pycallfault/pycallfault.h',
        'src/pycallfault/pycallfault.c',
    ]],
)

setuptools.setup(
    name         = 'stringcheese',
    version      = '1.1',
    description  = 'StringCheese is a tool to get easy CTF flags automatically.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url          = 'https://github.com/MathisHammel/stringcheese',
    author       = 'MathisHammel',
    author_email = 'e@e.e',
    license      = 'GPL2',
    ext_modules  = [module],
    packages     = ['stringcheese'],
    include_package_data=True,
    entry_points = {
        'console_scripts' : ['stringcheese=stringcheese.stringcheese:main']
    },
    install_requires = [
        'tqdm'
    ],
    zip_safe     = False
)
