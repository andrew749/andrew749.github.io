default:
	FLASK_APP=app.py flask run
db:
	python db_insert.py
