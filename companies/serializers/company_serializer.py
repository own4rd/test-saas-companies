from rest_framework import serializers
from companies.models.company import Company
from users.models.user import User


class CompanySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True
    )

    class Meta:
        model = Company
        fields = ["cnpj", "name", "trade_name", "user"]

    def create(self, validated_data):
        user = validated_data.pop("user")
        company = Company.objects.create(**validated_data)
        company.users.add(user)
        return company
