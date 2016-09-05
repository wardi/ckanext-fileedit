from os.path import basename
from importlib import import_module

import ckan.plugins as p
import json

from ckanext.fileedit.config import editable_files

class FileEditPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.IConfigurable)
    p.implements(p.IRoutes, inherit=True)

    def update_config(self, config):
        p.toolkit.add_ckan_admin_tab(
            config, 'edit_file_default', 'File Editor')
        p.toolkit.add_template_directory(config, 'templates')

    def configure(self, config):
        editable_files[:] = []  # in-place
        for c in json.loads(config['file_edit.editable_files']):
            editable_files.append({
                'path': c['path'],
                'label': c.get('label', basename(c['path'])),
                'validate': import_symbol(c.get('validate')) or nothing,
                'after_save': import_symbol(c.get('after_save')) or nothing,
            })

    def before_map(self, m):
        m.connect(
            'edit_file_default',
            '/ckan-admin/file-edit',
            action='edit_file_default',
            ckan_icon='wrench',
            controller='ckanext.fileedit.controller:FileEditController',
            )
        m.connect(
            '/ckan-admin/file-edit/{num}',
            action='edit_file',
            ckan_icon='wrench',
            controller='ckanext.fileedit.controller:FileEditController',
            )
        return m


def import_symbol(symbol_path):
    '''
    Given a path like "ckanext.mytheme.validators:file_validator"
    import the symbol file_validator from ckanext.mytheme.validators.

    Returns None if symbol_path is None.
    '''
    if symbol_path:
        module, symbol = symbol_path.split(':', 1)
        return getattr(import_module(module), symbol)

def nothing(*args, **kwargs):
    'do nothing'
