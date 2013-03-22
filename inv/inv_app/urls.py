from django.conf.urls import patterns, url

from inv_app import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^add_person/$', views.add_person, name='add_person'),
    url(r'^add_monitor/$', views.add_monitor, name='add_monitor'),
    url(r'^add_phone/$', views.add_phone, name='add_phone'),
    url(r'^add_printer/$', views.add_printer, name='add_printer'),
    url(r'^add_network/$', views.add_network, name='add_network'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^edit_person/(?P<id>\d+)/$', views.edit_person, name='edit_person'),
    url(r'^edit_monitor/(?P<id>\d+)/$', views.edit_monitor, name='edit_monitor'),
    url(r'^edit_phone/(?P<id>\d+)/$', views.edit_phone, name='edit_phone'),
    url(r'^edit_printer/(?P<id>\d+)/$', views.edit_printer, name='edit_printer'),
    url(r'^edit_network/(?P<id>\d+)/$', views.edit_network, name='edit_network'),
)