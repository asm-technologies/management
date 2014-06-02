from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from employee.views import *


urlpatterns = patterns("",
	
	url(r"^home/",'employee.views.home', name='home'),
	url(r"^employee/",'employee.views.employee', name='employee'),
	url(r"^projects/$",'employee.views.projects_main', name='projects_main'),
	url(r"^projects/(?P<proj_id>.+?)/$",'employee.views.projects', name='projects'),

	# url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
	# url(r"^employee/", TemplateView.as_view(template_name="employee.html"), name="employee"),
 #    url(r"^projects/", TemplateView.as_view(template_name="projects.html"), name="projects"),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)