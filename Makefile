default:
	FLASK_APP=app.py FLASK_DEBUG=true flask run --host=0.0.0.0
db:
	rm -f content.sqlite
	python db_insert.py
clean:
	rm -rf *.pyc

build_css:
	sass static/css/resume-styles.scss > static/css/resume-styles.css

