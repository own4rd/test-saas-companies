from rest_framework import serializers
from users.models.user import User
from ..exceptions.empty_users_id import EmptyUsersIDException
from users.exceptions.user_id_not_found import UserIdNotFoundException


class UserIDsValidator:
    def __call__(self, value):
        if len(value) == 0:
            raise EmptyUsersIDException()
        for user_id in value:
            try:
                User.objects.get(pk=user_id)
            except User.DoesNotExist:
                raise UserIdNotFoundException(
                    f"Usuário com o ID {user_id} não encontrado."
                )
