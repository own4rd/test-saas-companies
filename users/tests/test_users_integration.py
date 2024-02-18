import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_create_new_user_created_successfull(client):
    endpoint = reverse("users-list")
    payload = {
        "name": "Nome",
        "last_name": "Sobrenome",
        "email": "teste@2email.com",
        "password": "12345",
    }
    response = client.post(endpoint, payload)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.parametrize("field", ["name", "last_name", "password"])
@pytest.mark.django_db
def test_create_new_user_email_required_error(client, field):
    endpoint = reverse("users-list")
    payload = {
        "name": "Nome",
        "last_name": "Sobrenome",
        "email": "teste@email.com",
        "password": "12345",
    }
    del payload[field]

    response = client.post(endpoint, payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert field in response.data

    assert "Este campo é obrigatório." in response.data[field]


@pytest.mark.django_db
def test_create_new_user_existing_email_error(client, existing_user):
    endpoint = reverse("users-list")
    payload = {
        "name": "Nome",
        "last_name": "Sobrenome",
        "email": existing_user.email,
        "password": "12345",
    }
    response = client.post(endpoint, payload)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "email" in response.data
    assert "user com este email address já existe." in response.data["email"]
