from django.urls import path
from .views.companies_view import CompanyApiView, CompanyUserRegistrationApiView
from .views.detail_company_view import CompanyDetailApiView

urlpatterns_companies = [
    path("companies/", CompanyApiView.as_view(), name="create_company"),
    path("companies/<int:company_id>/users/", CompanyDetailApiView.as_view()),
    path(
        "companies/<int:company_id>/users/vinculate/",
        CompanyUserRegistrationApiView.as_view(),
    ),
]
