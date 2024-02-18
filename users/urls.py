from django.urls import path
from rest_framework.routers import DefaultRouter
from .views.user_viewset import UserViewSet
from .views.auth.user_companies_view import ListUserCompaniesApiView

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")
router_users = router.urls

# AUTH ROUTES
urlpatterns_users = router_users + [
    path("auth/user/companies", ListUserCompaniesApiView.as_view()),
]
