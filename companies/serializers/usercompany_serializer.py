from rest_framework import serializers
from companies.validators.user_ids_validator import UserIDsValidator


class UserCompanySerializer(serializers.Serializer):
    users_ids = serializers.ListField(
        child=serializers.IntegerField(), validators=[UserIDsValidator()]
    )
