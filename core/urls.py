from django.contrib import admin
from django.urls import path, include
from users.urls import urlpatterns_users
from companies.urls import urlpatterns_companies
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # API ROUTERS V1
    path("v1/", include(urlpatterns_users)),
    path("v1/", include(urlpatterns_companies)),
    # AUTH ROUTERS
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("admin/", admin.site.urls),
]
