from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("Poll/", include("Poll.urls")),
    path("admin/", admin.site.urls),
]