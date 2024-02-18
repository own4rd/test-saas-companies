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


@pytest.fixture
def mock_receita_service():
    mock_response_data = {
        "nome": "Novo Nome da Empresa",
        "fantasia": "Novo Nome Fantasia",
        "situacao": "Baixada",
    }

    with requests_mock.Mocker() as m:
        url = f"https://receitaws.com.br/v1/cnpj/123456789"
        m.get(url, json=mock_response_data)
        yield
