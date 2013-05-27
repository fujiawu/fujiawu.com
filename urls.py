from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from fujiawu.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', home),    
    url(r'^experience$', experience),    
    url(r'^research$', research),
    url(r'^publication$', publication),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico')),
    
)


urlpatterns += staticfiles_urlpatterns()

