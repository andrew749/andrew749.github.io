SERVER_FILE=app.py
PID=/tmp/andrewcodispoti.me.pid
HOST=0.0.0.0
RUN_COMMAND="flask run --host=$(HOST)"

serve:
	@echo "Starting Server"
	@fswatch -o . | xargs -n1 -I{} make build

build:
	docker build .

debug: _debug_env start

production: _prod_env start

_debug_env: _common_env
	@echo "DEBUG MODE ENABLED"
	export FLASK_DEBUG=true

_prod_env: _common_env
	@echo "PRODUCTION"
	export FLASK_DEBUG=false

_common_env:
	export FLASK_APP=$(SERVER_FILE)

start:
	@echo "Restarting"
	@$(RUN_COMMAND)

kill:
	@echo "KILLING SERVER with pid=`cat $(PID)`"
	@kill `cat $(PID)` || true
	@deactivate

rebuild_db: clean
	@echo "Rebuilding database"
	@python db_insert.py

clean:
	@echo "Cleaning pyc"
	@rm -rf *.pyc
	@echo "Removing Database"
	@rm -f content.sqlite

build_css:
	sass static/css/resume-styles.scss > static/css/resume-styles.css
