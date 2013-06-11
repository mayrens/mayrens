from django.conf.urls import patterns, url
from OffenseManagement.ManageOffense import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^site/$', views.site, name='site'),
    url(r'^sub_contractor/$', views.sub_contractor, name='sub_contractor'),
    url(r'^location/$', views.location, name='location'),
    url(r'^period/$', views.period, name='period'),
    url(r'^type/$', views.type, name='type'),
)