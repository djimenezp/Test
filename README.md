Mee gustaría ver una implementación de un CRUD de una tabla con elementos (id+descripción+marca) vinculados a una tabla
de propiedades (id+color) y una tabla de estado (id+descripción) y que era posible cambiar el estado de cada artículo.
Por ejemplo un artículo 1-Vestido-Zara, colores 1-negro y 2-blanco y, con estados 1-Listo para salir, 2-Alquilado,
3-Para ser limpiado

# Development

## Models

## Serializers

# Installation

### Dependencies

![Python](https://img.shields.io/badge/Python-3.9.2-greenyellow)
![Docker](https://img.shields.io/badge/Docker-3.9.2-blue)
![Django](https://img.shields.io/badge/Django-4.1.1-darkgreen)

Clone the repo

```sh
git clone git@github.com:djimenezp/InariBackendTest.git .
```

For non-production environment

```sh
docker-compose up -d --build
```

Server url will be in http://localhost:8000/

For production environment

```sh
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.yml exec web python manage.py migrate --noinput --settings project.prod
```

Server url will be in http://localhost/

# Questionary

