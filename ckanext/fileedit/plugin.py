import ckan.plugins as p

class FileEditPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.IRoutes, inherit=True)

    def update_config(self, config):
        p.toolkit.add_ckan_admin_tab(config, 'edit_file', 'File Editor')
        p.toolkit.add_template_directory(config, 'templates')

    def before_map(self, m):
        m.connect(
            'edit_file',
            '/ckan-admin/edit-config',
            action='edit_file',
            ckan_icon='wrench',
            controller='ckanext.fileedit.controller:FileEditController',
            )
        return m
