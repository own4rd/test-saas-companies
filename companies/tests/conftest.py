import pytest
import requests_mock
from django.contrib.auth import get_user_model


@pytest.fixture
def existing_user():
    User = get_user_model()
    user = User.objects.create(
        email="existing@example.com", name="New", last_name="User", password="12345"
    )
    return user
