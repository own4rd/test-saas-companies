from django.contrib import admin
from django.urls import path, include
from users.urls import urlpatterns_users
from .swagger_schema import schema_view
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
    # CONFIG ROUTERS
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("admin/", admin.site.urls),
]
