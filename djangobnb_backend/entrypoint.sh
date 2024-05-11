#!/bin/sh

if [ "$DATABASE" = "postgres" ] 
then
    echo "Check if database is running..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "The database is up and running :-D"
fi

python manage.py makemigrations
python manage.py migrate

exec "$@"
# Wait for the database to be ready
# echo "Waiting for the database to be ready..."
# if [ "$DATABASE" = "postgres" ]
# then
#     echo "Waiting for postgres..."

#     while ! nc -z $SQL_HOST $SQL_PORT; do
#         sleep 0.1
#     done

#     echo "PostgreSQL started ;-D"
# fi

# # Run the Django app
# python manage.py makemigrations
# python manage.py migrate

# exec "$@"
