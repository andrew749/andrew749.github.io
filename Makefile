# Flask configuration options
SERVER_FILE=app.py
HOST=0.0.0.0
FLASK_APP=$(SERVER_FILE)
RUN_COMMAND=FLASK_DEBUG=true FLASK_APP=$(SERVER_FILE) flask run --host=$(HOST)

serve:
	@echo "Starting Watching Server"
	@fswatch -o . | xargs -n1 -I{} make common_env

common_env: 

# different types of servers we can launch 
debug: _debug_env start
_debug_env: common_env
	@echo "Running debug server"
	@export FLASK_DEBUG=true

production: _prod_env start
_prod_env: common_env
	@echo "Running production server"
	@export FLASK_DEBUG=false

start:
	@echo "Restarting server"
	$(RUN_COMMAND)

rebuild_db: clean
	@echo "Rebuilding database"
	@python db_insert.py

clean:
	@echo "Cleaning compiled python files."
	rm -rf **/*.pyc
	@echo "Removing sqlite database"
	rm -f content.sqlite

.PHONY: common_env clean rebuild_db
