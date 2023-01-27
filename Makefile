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