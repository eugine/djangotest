from django.conf.urls import patterns, include, url

from django.contrib import admin
import esoapp
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangotest.views.home', name='home'),
    

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^eso/', include('esoapp.urls', namespace="esoapp")),
    url(r'^admin/', include(admin.site.urls)),
)
