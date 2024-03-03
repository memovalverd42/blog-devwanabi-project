
# Blog DevWanabi Project

Este es el proyecto de mi blog personal. 

El objetivo de este blog es publicar articulos sobre programación, microcontroladores y técnologia en general.



## Tech Stack


**Server:** Django, Postgresql, Celery, RabbitMQ


## Variables de entorno

To run this project, you will need to add the following environment variables to your .env file

Para poder correr el proyecto es necesario agregar las siguientes variables de entorno al archivo .env (tambien hay un .env.example de ejemplo).

Para la db (postgresql):

`DB_NAME`
`DB_USER`
`DB_PASSWORD`
`DB_HOST`
`DB_PORT`

Servicio de cloudinary:

`CLOUDINARY_CLOUD_NAME`
`CLOUDINARY_API_KEY`
`CLOUDINARY_API_SECRET`


## ¿Cómo correr el proyecto?

Clonar el repo

```bash
  git clone https://github.com/memovalverd42/blog-devwanabi-project
```

Entrar al repo

```bash
  cd blog-devwanabi-project
```

### Instalar dependencias

Instalar dependencias con pipenv

```bash
  pipenv install
```

Opcionalmente, puedes correr el servicio de la db y rabbitMQ en docker
con docker-compose

```bash
  docker-compose up -d
```

Crea el entorno virtual con pipenv

```bash
  pipenv shell
```

### Configuración inicial

```bash
  python manage.py migrate
```

```bash
  python manage.py createsuperuser
```

Opcionalmente puedes agregar alguna dumpdata inicial

```bash
  python manage.py loaddata posts_fixtures.json
```

### Ahora si, a correr el proyecto

Correr servicio de celery

```bash
  pipenv run run_celery
```

runserver

```bash
  pipenv run run
```
