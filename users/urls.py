from django.urls import path
from rest_framework.routers import DefaultRouter
from .views.user_viewset import UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")
router_users = router.urls

# AUTH ROUTES
urlpatterns_users = router_users
