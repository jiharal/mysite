install:
	@pipenv install -r requirements.txt
update-req:
	@pipenv run pip3 freeze > requirements.txt
start:
	@python3 manage.py runserver
test:
	@DJANGO_SETTINGS_MODULE="mysite.settings_test" python3 manage.py test ${arg} --keepdb -v 3
migrate:
	@python3 manage.py makemigrations 
	@python3 manage.py migrate
new-app:
	@python3 manage.py startapp ${arg}
shell:
	@pipenv shell