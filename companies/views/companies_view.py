from rest_framework.views import APIView
from companies.serializers.company_serializer import CompanySerializer
from rest_framework.response import Response
from rest_framework import status
from companies.models.company import Company
from users.models.user import User
from companies.serializers.usercompany_serializer import UserCompanySerializer
from companies.exceptions.company_not_found_exception import CompanyNotFoundException
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class CompanyApiView(APIView):
    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyUserRegistrationApiView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "users_ids": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_INTEGER),
                )
            },
        )
    )
    def post(self, request, company_id):
        users = []
        try:
            company = Company.objects.get(pk=company_id)
        except Company.DoesNotExist:
            raise CompanyNotFoundException()

        serializer = UserCompanySerializer(data=request.data)
        if serializer.is_valid():
            user_ids = serializer.validated_data.get("users_ids", [])
            users = User.objects.filter(pk__in=user_ids)
            company.users.add(*users)
            return Response(
                {"message": "Usuário(s) cadastrado(s) com sucesso."},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
