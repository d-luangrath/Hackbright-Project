SHELL := /bin/bash

run:
	@echo "Starting server..."
	python3 server.py

seed:
	@echo "Seeding DataBase..."
	python3 seed_database.py

drop_db:
	@echo "Dropping DB 'recipes'..."
	dropdb recipes

create_db:
	@echo "Creating DB 'recipes'..."
	createdb recipes
	python3 model.py -c "db.create_all()"

bootstrap:
	@echo -e "\033[32mBootstrapping DB from the dump file...\033[0m"
	psql recipes < bootstrap.sql

recreate_db: drop_db create_db seed
	@echo "DB is recreated!"

show_users:
	psql -c "SELECT * FROM users;" recipes

docker_img:
	docker build -t hbproject-image .

docker_run:
	docker run \
		--name hbproject-container \
		--interactive \
		--tty \
		--rm \
		-p 8000:8000 \
		-v ~/projects/hbproject:/app \
		hbproject-image

sh:
	docker exec -it hbproject-container bash

build:
	docker-compose build

up:
	docker-compose up --remove-orphans

down:
	docker-compose down --remove-orphans

restart:
	make down
	make up

logs:
	docker-compose logs