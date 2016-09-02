import ckan.plugins as p

class ConfigEditPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.IRoutes, inherit=True)

    def update_config(self, config):
        p.toolkit.add_ckan_admin_tab(config, 'edit_config', 'Edit Schema')

    def before_map(self, m):
        m.connect(
            'edit_config',
            '/ckan-admin/edit-config',
            action='edit_config',
            ckan_icon='wrench',
            controller='ckanext.configedit.controller:ConfigEditController',
            )
        return m
