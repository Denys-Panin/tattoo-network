MANAGE = python src/manage.py

start:
	$(MANAGE) runserver

mm:
	$(MANAGE) makemigrations

m:
	$(MANAGE) migrate

user:
	$(MANAGE) createsuperuser
