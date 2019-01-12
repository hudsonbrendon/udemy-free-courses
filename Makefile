################################################################################
# Docker-compose django service commands for dev
################################################################################

migrate.docker:
	docker-compose run django python manage.py migrate

makemigrations.docker:
	docker-compose run django python manage.py makemigrations

collectstatic:
	docker-compose run django python manage.py collectstatic

test:
	docker-compose run django python manage.py test $(app)

coverage:
	docker-compose run django coverage run --source='.' manage.py test $(app)
	docker-compose run django coverage report

shell.docker:
	docker-compose run django python manage.py shell

createusers.docker:
	docker-compose run django python manage.py createusers --r --a --su

up:
	docker-compose up

logs:
	docker-compose logs

down:
	docker-compose down

build:
	docker-compose build

start:
	docker-compose start

stop:
	docker-compose stop

################################################################################
# Heroku cli and deploy commands for prod
################################################################################

deploy.prod:
	git push heroku dev:master

migrate.prod:
	heroku run python manage.py migrate --app udemy-free-courses

makemigrations.prod:
	heroku run python manage.py makemigrations --app udemy-free-courses

shell.prod:
	heroku run python manage.py shell --app udemy-free-courses

createusers.prod:
	heroku run python manage.py createusers --r --a --su --app udemy-free-courses