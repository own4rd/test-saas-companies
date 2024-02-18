import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_create_new_company_created_successfull(client, existing_user):
    endpoint = reverse("create_company")
    payload = {
        "cnpj": "00000001001",
        "name": "Testing Enterprise",
        "trade_name": "Testing",
        "user": existing_user.id,
    }
    response = client.post(endpoint, payload)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_create_new_company_user_not_existing(client):
    endpoint = reverse("create_company")
    payload = {
        "cnpj": "00000001001",
        "name": "Testing Enterprise",
        "trade_name": "Testing",
        "user": 999,
    }
    response = client.post(endpoint, payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'Pk inválido "999" - objeto não existe.' in response.data["user"]


@pytest.mark.django_db
def test_create_new_company_created_fail_without_user(client):
    endpoint = reverse("create_company")
    payload = {
        "cnpj": "00000001001",
        "name": "Testing Enterprise",
        "trade_name": "Testing",
    }
    response = client.post(endpoint, payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "Este campo é obrigatório." in response.data["user"]
