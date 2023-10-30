run:
	python3 manage.py runserver

update_msg:
	django-admin makemessages -a

compil_msg:
	django-admin compilemessages

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

test:
	./manage.py test

lint:
	poetry run flake8 .

test-coverage:
		poetry run pytest --cov=. --cov-report xml tests


install:
	poetry install