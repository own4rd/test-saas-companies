import pytest
from companies.models.company import Company


@pytest.mark.django_db
def test_update_company_by_receita_service(mock_receita_service):
    company = Company.objects.create(
        cnpj="123456789", name="Old Name", trade_name="Old Trade Name", status="Ativo"
    )
    company.update_company_service()

    assert company.name == "Novo Nome da Empresa"
    assert company.trade_name == "Novo Nome Fantasia"
    assert company.status == "Baixada"
