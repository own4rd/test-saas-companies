
# Test SaaS Companies

O presente projeto objetiva a simulação de um microSaaS para gerenciamento de Empresas e Usuários

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

## Documentação
A api utiliza Swagger para documentação. Este pode ser acessado através do link /swagger. Exemplo: http://localhost:8000/swagger/
