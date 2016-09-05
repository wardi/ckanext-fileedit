from subprocess import Popen, PIPE

from ckan.plugins.toolkit import h

def apache_graceful_restart(f):
    'example after_update function'
    out, err = Popen(['/usr/sbin/apachectl', '-k', 'graceful'],
        stdout=PIPE, stderr=PIPE).communicate()
    if err:
        h.flash_error(unicode(err))
