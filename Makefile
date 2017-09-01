debug:
	FLASK_APP=app.py FLASK_DEBUG=true flask run --host=0.0.0.0

build_css:
	sass static/css/resume-styles.scss > static/css/resume-styles.css
