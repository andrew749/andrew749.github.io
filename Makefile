default:
	FLASK_APP=app.py flask run
db:
	rm -f content.sqlite
	python db_insert.py
