
run:
	docker-compose build
	docker-compose  up  -d --remove-orphans

init:
	docker-compose exec server alembic revision --autogenerate -m "message"
	docker-compose exec server alembic upgrade head

stop:
	docker-compose down

test:
	coverage run  -m pytest tests/
	coverage report -m
	
pre-com:
	pre-commit install

