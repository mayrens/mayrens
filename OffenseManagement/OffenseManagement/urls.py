from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin 
from django.contrib.sites.models import Site

admin.autodiscover()
admin.site.unregister(Site)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OffenseManagement.views.home', name='home'),
    # url(r'^OffenseManagement/', include('OffenseManagement.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^offences/', include('OffenseManagement.ManageOffense.urls')),
)
