from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^Employees/$', 'Employees.views.index'), #View all employees
	url(r'^Employees/(\d{1,3})/$', 'Employees.views.index'), #To do - for viewing an individual employee by there id number
	url(r'^Clients/$', 'Employees.views.index'), #View all employees
	url(r'^Clients/(\d{1,3})/$', 'Employees.views.index'), #To do - for viewing an individual client by there id number
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
)
