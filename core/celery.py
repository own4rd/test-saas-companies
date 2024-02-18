# celery.py

import os
from celery import Celery

# Define o nome da aplicação Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery("core")

# Configura a aplicação Celery
app.config_from_object("django.conf:settings", namespace="CELERY")

# Carrega as tarefas da aplicação Django
app.autodiscover_tasks()
