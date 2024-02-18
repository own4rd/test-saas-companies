from rest_framework.views import APIView
from companies.serializers.company_serializer import CompanySerializer
from rest_framework.response import Response
from rest_framework import status


class CompanyApiView(APIView):
    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
