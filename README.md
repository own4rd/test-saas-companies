
# SaaS Companies

O presente projeto objetiva a simulação de um microSaaS para gerenciamento de Empresas e Usuários

## Dependências

- Django 4+
- Celery 5+
- Redis 5+

## Configuração

### Docker
Instale os containers necessários para aplicação (Postgres e Redis):

```bash
  docker-compose up -d
```

Lembre-se de criar um banco no container do postgres:

```bash
  docker exec -it db bash
```
```bash
  psql -U postgres[ou seu usuário]
```
```bash
  CREATE DATABASE seu_banco;
```
### Python
Crie sua env e instale as requirements: 
```bash
  pip install -r requirements.txt
```
Altere o arquivo .env-example para '.env' e insira suas configurações.

Agora só executar as migrations:
```bash
  python manage.py migrate
```

### Celery
Para iniciar o worker, utilize o seguinte comando no terminal:
```bash
celery -A core worker --loglevel=info
```
Para iniciar o beat (celery-beat), utilize o seguinte comando:
```bash
celery -A core beat -l info
```

## Documentação
A api utiliza Swagger para documentação. Este pode ser acessado através do link /swagger. Exemplo: http://localhost:8000/swagger/
