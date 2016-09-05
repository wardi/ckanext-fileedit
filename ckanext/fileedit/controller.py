from ckan.plugins.toolkit import (
    _, BaseController, check_access, NotAuthorized, abort, render,
    )

class FileEditController(BaseController):
    def __before__(self, action, **params):
        super(FileEditController, self).__before__(action, **params)
        try:
            check_access('sysadmin', {})
        except NotAuthorized:
            abort(403, _('Need to be system administrator to administer'))

    def edit_file(self):
        return render('fileedit/edit.html', extra_vars={
            'data': {}, 'errors': {}
            })
