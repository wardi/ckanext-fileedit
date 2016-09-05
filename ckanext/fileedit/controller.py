import re

from ckan.plugins.toolkit import (
    _, BaseController, check_access, NotAuthorized, abort, render, redirect_to
    )

from ckanext.fileedit.config import editable_files


class FileEditController(BaseController):
    def __before__(self, action, **params):
        super(FileEditController, self).__before__(action, **params)
        try:
            check_access('sysadmin', {})
        except NotAuthorized:
            abort(403, _('Need to be system administrator to administer'))

    def edit_file_default(self):
        redirect_to(
            controller='ckanext.fileedit.controller:FileEditController',
            action='edit_file',
            num='0')

    def edit_file(self, num):
        if not re.match(r'^\d+$', num):
            abort(404, _('Not found'))
        num = int(num)
        f = editable_files[num]
        return render('fileedit/edit.html', extra_vars={
            'data': {}, 'errors': {}, 'editable_files': editable_files,
            'label': f['label'], 'num': num,
            })
