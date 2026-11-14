from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from .views import healthz

admin.site.site_header = "GA Timesheet admin"
admin.site.site_title = "GA Timesheet"

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("healthz", healthz, name="healthz"),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]
