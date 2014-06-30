from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

from account.views import SignupView, LoginView, LogoutView, DeleteView

admin.autodiscover()

urlpatterns = patterns("",
	url(r"^$", LoginView.as_view(), name="account_login"),
	url(r'', include('employee.urls')),
    url(r"^admin/", include(admin.site.urls)),
    url(r'', include("account.urls")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
