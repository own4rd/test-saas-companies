from celery import shared_task
from companies.models.company import Company
from datetime import date
import logging


@shared_task
def update_company_info_task():
    logging.getLogger("Start Updating Companies")
    current_date = date.today()
    companies_to_update = Company.objects.filter(data_updated_at=current_date)
    for company in companies_to_update:
        company.update_company_service()
    logging.getLogger("End Updating Companies")
