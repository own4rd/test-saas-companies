from django.urls import path
from .views.companies_view import CompanyApiView, CompanyUserRegistrationApiView


urlpatterns_companies = [
    path("companies/", CompanyApiView.as_view(), name="create_company"),
    path(
        "companies/<int:company_id>/users/vinculate/",
        CompanyUserRegistrationApiView.as_view(),
    ),
]
