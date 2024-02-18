from rest_framework import serializers
from users.models.user import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "last_name", "name", "password"]

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data["email"],
            name=validated_data["name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
