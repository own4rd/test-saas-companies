from django.db import models
from datetime import timedelta
from django.utils import timezone

from users.models.user import User


def thirty_days_from_now():
    return timezone.now() + timedelta(days=30)


class Company(models.Model):
    cnpj = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    trade_name = models.CharField(max_length=255)
    users = models.ManyToManyField(User)
    status = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    data_updated_at = models.DateField(default=thirty_days_from_now)

    def __str__(self) -> str:
        return f"{self.name} - {self.cnpj}"

    def update_company_service(self):
        import requests
        response = requests.get(f"https://receitaws.com.br/v1/cnpj/{self.cnpj}")
        data = response.json()
        self.name = data["nome"]
        self.trade_name = data["fantasia"]
        self.status = data["situacao"]
        self.updated_at = timezone.now()
        self.data_updated_at = thirty_days_from_now()
        self.save()
