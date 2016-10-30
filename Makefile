default:
	FLASK_APP=app.py FLASK_DEBUG=true flask run
db:
	rm -f content.sqlite
	python db_insert.py
