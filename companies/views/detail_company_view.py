from rest_framework.views import APIView
from rest_framework.response import Response
from companies.models.company import Company
from users.serializers.user_serializer import UserSerializer


class CompanyDetailApiView(APIView):
    def get(self, request, company_id):
        company = Company.objects.get(pk=company_id)
        users = company.users.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data)
