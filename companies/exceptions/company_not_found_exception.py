from rest_framework.exceptions import APIException


class CompanyNotFoundException(APIException):
    status_code = 404
    default_detail = "A empresa não existe."
    default_code = "company_not_found"
