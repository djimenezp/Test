Me gustaría ver una implementación de un CRUD de una tabla con elementos (id+descripción+marca) vinculados a una tabla
de propiedades (id+color) y una tabla de estado (id+descripción) y que era posible cambiar el estado de cada artículo.
Por ejemplo un artículo 1-Vestido-Zara, colores 1-negro y 2-blanco y, con estados 1-Listo para salir, 2-Alquilado,
3-Para ser limpiado

# Installation

### Dependencies

![Python](https://img.shields.io/badge/Python-3.9.2-greenyellow)
![Docker](https://img.shields.io/badge/Docker-3.9.2-blue)
![Django](https://img.shields.io/badge/Django-4.1.1-darkgreen)

#### To clone the repo use:

```sh
git clone git@github.com:djimenezp/Test.git .
```

#### For non-production environment use:

```sh
docker-compose up -d --build
```

Server url will be in http://localhost:8000/

#### For production environment use:

```sh
docker-compose -f docker-compose.prod.yml up -d --build
```

Server url will be in http://localhost/

#### For adding initial user use:

```sh
#dev
docker-compose -f docker-compose.yml exec web python manage.py createsuperuser
#prod
docker-compose -f docker-compose.prod.yml  exec web python manage.py createsuperuser --settings project.prod
```

# Usage

#### For using Django Admin Site go to _/admin/_

#### For using Django Rest Framework site go to _/api/_

