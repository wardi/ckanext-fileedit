#!/usr/bin/env/python
from setuptools import setup

setup(
    name='ckanext-configedit',
    version='0.1',
    description='',
    license='AGPL3',
    author='',
    author_email='',
    url='',
    namespace_packages=['ckanext'],
    packages=['ckanext.configedit'],
    zip_safe=False,
    entry_points = """
        [ckan.plugins]
        configedit = ckanext.configedit.plugin:ConfigEditPlugin
    """
)
