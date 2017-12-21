SERVER_FILE=app.py
HOST=0.0.0.0
FLASK_APP=$(SERVER_FILE)
RUN_COMMAND=FLASK_APP=$(SERVER_FILE) flask run --host=$(HOST)

# CSS Compile options
CSS_C=sass
CSS_FLAGS=

# directories to compile scss
SCSS_SRC=static/scss
CSS_OUT=static/css
CSS_TARGETS=$(patsubst $(SCSS_SRC)/%.scss,%.css,$(wildcard $(SCSS_SRC)/*.scss))

serve:
	@echo "Starting Watching Server"
	@fswatch -o . | xargs -n1 -I{} make build

build:
	docker build .

%.css: $(SCSS_SRC)/%.scss
	sass $< $(CSS_OUT)/$(notdir $@)

common_env: $(CSS_TARGETS)

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
	rm -rf *.pyc
	@echo "Removing sqlite database"
	rm -f content.sqlite

.PHONY: common_env clean rebuild_db
