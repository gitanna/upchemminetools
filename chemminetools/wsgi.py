#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
WSGI config for chemminetools project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""

import os,sys



import site
#AA
site.addsitedir('/opt/portal/python-environments/chem-dev/lib/python2.7/site-packages')

sys.path.append('/vagrant/projects/chemminetools')
sys.path.append('/vagrant/projects/chemminetools/chemminetools')

from django.core.wsgi import get_wsgi_application

activate_this = '/opt/portal/python-environments/chem-dev/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chemminetools.settings")

application = get_wsgi_application()
