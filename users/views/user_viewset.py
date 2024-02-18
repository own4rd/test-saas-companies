from rest_framework.viewsets import ModelViewSet
from users.serializers.user_serializer import UserSerializer
from users.models.user import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
