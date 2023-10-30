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
	poetry run python ./manage.py test --verbosity 2

lint:
	poetry run flake8 .

test-coverage:
		poetry run coverage run --cov=. --cov-report xml manage.py test


install:
	poetry install