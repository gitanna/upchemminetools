#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf.urls import *
from django.contrib import admin
from django.conf import settings
#from django.views.generic.simple import direct_to_template
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from django.contrib.auth.views import login, logout
import os

# enable cron

#import django_cron
#django_cron.autodiscover()
print '\n in urls before autodiscorver'
admin.autodiscover()
print '\n in urls after autodiscorver'

urlpatterns =[
   #AA r'',
    url(r'^admin/', admin.site.urls),
  #  (r'^eisearch/', include('eisearch.urls')),
  #  (r'^accounts/', include('userena.urls')),
  ##  url(r'^compounds/',include('compounddb.urls')),
   ## url(r'^my[Cc]ompounds/',include('myCompounds.urls')),
  #  (r'^tools/', include('tools.urls')),
  #  (r'^search/?',  RedirectView.as_view(url='/eisearch/query/')),
  #  (r'^similarity/', include('similarityworkbench.urls')),
   # (r'^ChemmineR/', include('ChemmineR.urls')),
 #   (r'^robots\.txt/?$', direct_to_template, {'template': 'robots.txt',
 #    'content-type': 'text/plain'}),
 #   (r'^ei/?',  RedirectView.as_view(url='/downloads/')),
   #AA url(r'^', cms.urls)
    ]

# AA if settings.DEBUG:
#     urlpatterns = [r'', url(r'^working/(?P<path>.*)$',
#                            r'django.views.static.serve',
#                            {'document_root': settings.MEDIA_ROOT,
#                            'show_indexes': False}),
#                            url(r'',
#                            include(r'django.contrib.staticfiles.urls'
#                            ))] + urlpatterns
print '\n os.environ chemminetools.setting ', settings

print '\n in urls after admin'