from django.contrib import admin
from django.urls import path, include
from users.urls import urlpatterns_users

urlpatterns = [
    # API ROUTERS V1
    path("v1/", include(urlpatterns_users)),
    path("admin/", admin.site.urls),
]
