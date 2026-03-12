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
    raise ValueError("Python %s is not supported" % python_version)

## Reading long_description
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="stringcheese",
    version="2.1",
    description="StringCheese is a tool to get easy CTF flags automatically.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MathisHammel/stringcheese",
    author="MathisHammel",
    author_email="mathis@h25.io",
    license="GPL2",
    packages=["stringcheese"],
    include_package_data=True,
    entry_points={"console_scripts": ["stringcheese=stringcheese.stringcheese:main"]},
    install_requires=["tqdm", "ahocorasick-rs"],
    zip_safe=False,
)
