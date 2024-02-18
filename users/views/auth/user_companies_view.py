from rest_framework.views import APIView
from companies.serializers.company_serializer import CompanySerializer
from rest_framework.response import Response
from companies.serializers.company_serializer import CompanySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ListUserCompaniesApiView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            200: openapi.Response("List of companies", CompanySerializer(many=True))
        },
        security=[{"Bearer": []}],
    )
    def get(self, request):
        user = request.user
        companies = user.company_set.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
