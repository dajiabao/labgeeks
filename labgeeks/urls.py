from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to
import forms_builder.forms.urls
import os
import settings
import forms_builder.forms.urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # (r'^accounts/login/$', 'django.contrib.auth.views.login'),
                       (r'^login/$', 'labgeeks.views.labgeeks_login'),
                       (r'^logout/$', 'labgeeks.views.labgeeks_logout'),
                       (r'^inactive/$', 'labgeeks.views.inactive'),
                       # Example:
                       # (r'^labgeeksrpg/', include('labgeeksrpg.foo.urls')),
                       (r'^chronos/', include('labgeeks_chronos.urls')),
                       (r'^people/', include('labgeeks_people.urls')),
                       (r'^schedule/', include('labgeeks_horae.urls')),
                       # (r'^delphi/', include('labgeeks_delphi.urls')),
                       # (r'^pythia/', include('labgeeks_pythia.urls')),
                       # (r'^oracles/', include('labgeeks_sybil.urls')),
                       (r'^tools/', include('labgeeks_apollo.urls')),
                       (r'^$', 'labgeeks.views.hello'),
                       (r'^badger/', include('badger.urls')),
                       (r'^pages/', 'labgeeks.views.pages'),
                       # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
                       # to INSTALLED_APPS to enable admin documentation:
                       # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       (r'^admin/', include(admin.site.urls)),
                       (r'^forms/', include(forms_builder.forms.urls)),
                       )

# only serve static files through the django server if debug is enabled. Only for development instances.
if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
                            )
