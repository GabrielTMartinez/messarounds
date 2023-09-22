# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

setup(
    name='basicSite',
    version='0.1.0',
    description='Personal Django framework test',
    long_description=readme,
    author='Gabriel TM',
    author_email='',
    url='',
    license=None,
    packages=find_packages(exclude=('tests', 'docs'))
)
