import pytest
from users.serializers.user_serializer import UserSerializer


@pytest.mark.django_db
def test_user_serializer_is_valid(valid_user_data):
    serializer = UserSerializer(data=valid_user_data)
    assert serializer.is_valid()


@pytest.mark.django_db
def test_user_serializer_is_invalid(invalid_user_data):
    serializer = UserSerializer(data=invalid_user_data)
    assert not serializer.is_valid()


@pytest.mark.django_db
def test_user_serializer_invalid_data():
    invalid_user_data = {
        "email": "my_email_invalid",
        "name": "Test",
        "last_name": "Tester",
        "password": "12345",
    }
    serializer = UserSerializer(data=invalid_user_data)
    assert not serializer.is_valid()
    assert "email" in serializer.errors
