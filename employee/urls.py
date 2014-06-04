from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from employee.views import *


urlpatterns = patterns("",
	url(r"^home/",'employee.views.home', name='home'),
	url(r"^employee/$",'employee.views.employees_main', name='employees_main'),
	url(r"^employee/(?P<emp_id>.+?)/$",'employee.views.employees', name='employees'),
	url(r"^projects/$",'employee.views.projects_main', name='projects_main'),
	url(r"^projects/(?P<proj_id>.+?)/$",'employee.views.projects', name='projects'),

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
