#!/usr/bin/env/python
from setuptools import setup

setup(
    name='ckanext-fileedit',
    version='0.1',
    description='',
    license='AGPL3',
    author='',
    author_email='',
    url='',
    namespace_packages=['ckanext'],
    packages=['ckanext.fileedit'],
    zip_safe=False,
    entry_points = """
        [ckan.plugins]
        file_edit = ckanext.fileedit.plugin:FileEditPlugin
    """
)
