from django.conf.urls import patterns, url
import seacher.views as views
import settings

urlpatterns = patterns('',
                       (r'^web', views.mainweb),
                       url(r'^staticfiles/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.STATICFILES_DIRS, 'show_indexes': True}),
                       (r'^images', views.image),
)
