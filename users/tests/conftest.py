import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def existing_user():
    User = get_user_model()
    user = User.objects.create(
        email="existing@example.com", name="New", last_name="User", password="12345"
    )
    return user


@pytest.fixture
def valid_user_data():
    return {
        "email": "test@example.com",
        "name": "Test",
        "last_name": "Tester",
        "password": "12345",
    }


@pytest.fixture
def invalid_user_data():
    return {"name": "Test", "last_name": "Tester", "password": "12345"}
