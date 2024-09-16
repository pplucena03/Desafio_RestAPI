# API de Tarefas com Integração ao Google Calendar
Este projeto é uma API RESTful desenvolvida em Python, utilizando Django e Django REST Framework. A API permite a criação, com integração ao Google Calendar para adicionar e remover eventos. O projeto segue as melhores práticas.

# Funcionalidades
## CRUD completo de tarefas:
- Título (obrigatório)
- Descrição (opcional)
- Data (obrigatória)
- Horário (opcional)

## Integração com o Google Calendar para criação de eventos.
### Busca de tarefas por:
- ID
- Período de datas
- Título (com suporte a busca por palavras parciais e texto composto).

# Tecnologias Utilizadas
- Python
- Django (versão LTS)
- Django REST Framework (versão LTS)
- Google Calendar API (para integração com o calendário)
- Insomnia (para testar a API)

# Requisitos
- Python 3.x
- Django 3.x ou superior
- Django REST Framework
- Dependências do Google Calendar 
(tudo listado no requirements.txt)

# Instalação e execução
## Clone o repositório
git clone https://github.com/pplucena03/desafio_tecnico

## Crie um ambiente virtual
python -m venv .venv \
source venv/bin/activate (Para Linux/macOS) \
.\.venv\Scripts\activate (Para Windows)

## Instale as dependências
pip install -r requirements.txt

## Configure a API do Google
- Siga o guia rápido para obter as credenciais -> https://developers.google.com/calendar/api/quickstart/python
- Coloque o arquivo credentials.json na pasta do projeto.

## Migração do banco de dados
python manage.py makemigrations
python manage.py migrate

## Inicializando o servidor
python manage.py runserver

# Testando a API
- Você pode utilizar o Insomnia ou qualquer outra ferramenta de API para testar os endpoints.

# Diferenciais
- Autenticação JWT: Implementação de autenticação usando JSON Web Tokens.