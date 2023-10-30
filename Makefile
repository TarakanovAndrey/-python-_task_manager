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
			@poetry run coverage run --source='.' manage.py test
			@poetry run coverage report
			@poetry run coverage xml


install:
	poetry install