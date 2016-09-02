from ckan.plugins import toolkit, IConfigurer, SingletonPlugin, implements

class ConfigEditPlugin(SingletonPlugin):
    implements(IConfigurer)

    def update_config(self, config):
        pass
