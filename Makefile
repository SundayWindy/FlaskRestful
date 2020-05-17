
run:
	docker-compose  up  -d

init:
	docker-compose exec server alembic upgrade head

stop:
	docker-compose down