#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import *
from views import compound_detail
from views import cid_lookup
#from views import render_image

urlpatterns = [url(r'^cid_lookup/?$',
                       cid_lookup, name='cid_lookup'),
                      # url(r'^(?P<id>\d+)/png/?(?P<filename>\S*)$',
                       #'compounddb.views.render_image'),
                       url(r'^(?P<id>\d+)/(?P<resource>\w*)/?(?P<filename>\S*)$'
                       , compound_detail,
                       name='compound_detail')]
