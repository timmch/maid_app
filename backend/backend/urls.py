from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^Employees/$', 'Employees.views.index'),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
)
