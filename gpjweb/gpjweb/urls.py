from django.conf.urls import patterns, include, url
import seacher.views as views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^test/$', views.testweb),
    # Examples:
    # url(r'^$', 'gpjweb.views.home', name='home'),
    # url(r'^gpjweb/', include('gpjweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
