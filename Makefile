default:
	FLASK_APP=app.py flask run
db:
	rm content.sqlite
	python db_insert.py
