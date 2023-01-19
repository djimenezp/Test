#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input --settings project.prod
python manage.py makemigrations --settings project.prod
python manage.py migrate --settings project.prod
python manage.py collectstatic --no-input --clear --settings project.prod

exec "$@"