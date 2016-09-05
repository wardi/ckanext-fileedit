import re
import codecs

from ckan.plugins.toolkit import (
    _, h, BaseController, check_access, NotAuthorized, abort, render,
    redirect_to, request,
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
        errors = {}
        if request.POST:
            contents = request.POST['contents']
            err = file_edit_update(num, contents)
            if not err:
                h.flash_success(_("File Updated"))
                redirect_to(
                    controller='ckanext.fileedit.controller:FileEditController',
                    action='edit_file',
                    num='0')
            errors['contents'] = [err]
        else:
            contents = file_edit_show(num)

        return render('fileedit/edit.html', extra_vars={
            'data': {'contents': contents},
            'errors': errors,
            'editable_files': editable_files,
            'label': f['label'],
            'num': num,
            })


# FIXME: make these logic functions so they're usable from the API
def file_edit_show(num):
    f = editable_files[num]
    # r+ to make sure we can write it
    with codecs.open(f['path'], 'r+', 'utf-8') as cf:
        return cf.read()

def file_edit_update(num, contents):
    f = editable_files[num]
    err = f['validate'](f, contents)
    if err:
        return err
    with codecs.open(f['path'], 'w', 'utf-8') as cf:
        cf.write(contents)
    f['after_update'](f)
