from rest_framework.exceptions import APIException


class EmptyUsersIDException(APIException):
    status_code = 400
    default_detail = "Lista de usuários vazia."
    default_code = "user_id_not_found"
