# Bookstore

Bookstore APP from Backend Python course from EBAC
Este projeto é uma API RESTful para gerenciamento de uma livraria, construída com **Django**, **Django REST Framework**, **Docker**, **Poetry** e testada com **pytest**.

## Tecnologias Utilizadas

- Python 3.10+
- Django 5.x
- Django REST Framework
- PostgreSQL (via Docker)
- Docker e Docker Compose
- Poetry (gerenciador de dependências)
- Pytest (para testes automatizados)

---

## Prerequisites

```

- Python >= 3.10  
- [Poetry](https://python-poetry.org/docs/#installation)
- [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/)


```

## Quickstart

1. Clone this project

   ```
   git clone git@github.com:DeniseGrassi/BOOKSTORE.git
   cd bookstore
   ```
   
2. Install dependencies:

   ```
   cd bookstore
   poetry install
   ```

3. Run local dev server:

   ```
    poetry run python manage.py migrate
    poetry run python manage.py runserver

   ```
   
4. Run docker dev server environment:

   ```
   docker-compose up -d --build 
   docker-compose exec web python manage.py migrate
   ```

5. Run tests inside of docker:

   ```
    poetry run python manage.py test

    docker-compose exec web python manage.py test
   ```

6. Deploy automático para o Heroku configurado via GitHub Actions