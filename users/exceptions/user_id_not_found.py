from rest_framework.exceptions import APIException


class UserIdNotFoundException(APIException):
    status_code = 404
    default_detail = "O usuário não existe."
    default_code = "user_not_found"
