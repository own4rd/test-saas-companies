from django.urls import path
from .views.companies_view import CompanyApiView


urlpatterns_companies = [
    path("companies/", CompanyApiView.as_view(), name="create_company"),
]
