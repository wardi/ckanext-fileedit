from ckan.plugins.toolkit import (
    _, BaseController, check_access, NotAuthorized, abort, render,
    )

class ConfigEditController(BaseController):
    def __before__(self, action, **params):
        super(ConfigEditController, self).__before__(action, **params)
        try:
            check_access('sysadmin', {})
        except NotAuthorized:
            abort(403, _('Need to be system administrator to administer'))

    def edit_config(self):
        return render('configedit/edit.html', extra_vars={
            'data': {}, 'errors': {}
            })
