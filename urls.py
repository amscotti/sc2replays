from django.conf.urls.defaults import patterns, include, url
# from sc2replays.views import *
from sc2replays.display import views
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	('^$', views.home),

	(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),

    # Examples:
    # url(r'^$', 'sc2replays.views.home', name='home'),
    # url(r'^sc2replays/', include('sc2replays.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
