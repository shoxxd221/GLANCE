# GLANCE

docker-compose exec django python manage.py makemigrations --noinput

docker-compose exec django python manage.py migrate --noinput

py manage.py spectacular --file schema.yml