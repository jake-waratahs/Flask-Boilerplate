# Determine the DB Driver
CONFIG_TYPE=`python Application/config`
DB_DATABASE=`python Application/config -k DB_DATABASE`
DB_DATABASE_DRIVER=`python Application/config -k DB_DRIVER`

DB_USER=`python Application/config -k DB_USERNAME`
DB_BASE=`python Application/config -k DB_BASE`

RUN_SCRIPT='app'
RUN_TEST_SCRIPT='test.py'

PYTHON_BINARY=`which python3`
VENV_LOCATION=.venv
VENV_ACTIVATE="$(VENV_LOCATION)/bin/activate"

all: debug

debug: venv regenerate db
	. $(VENV_ACTIVATE); python $(RUN_SCRIPT) server $(ARGS) --debug 


test: venv regenerate db
	. $(VENV_ACTIVATE); python $(RUN_TEST_SCRIPT)


clean:
	if [ "$(CONFIG_TYPE)" = "MySQLStd" ]; then echo "DROP DATABASE IF EXISTS $(DB_DATABASE);" | mysql -u $(DB_USER); fi
	if [ "$(CONFIG_TYPE)" = "CI" ]; then echo "DROP DATABASE IF EXISTS $(DB_DATABASE);" | mysql -u $(DB_USER); fi
	rm -rf ./Application/$(DB_BASE).db
	rm -rf $(VENV_LOCATION)/.db


# Regenerate static files
regenerate:
	./util/compile.sh ./Application/static/css
	./util/regenerate.sh ./Application/models Model
	./util/regenerate.sh ./Application/views View

uninstall: clean
	rm -rf $(VENV_LOCATION)

db: venv $(VENV_LOCATION)/.db
$(VENV_LOCATION)/.db:
	if [ "$(CONFIG_TYPE)" = "MySQLStd" ]; then echo "CREATE DATABASE IF NOT EXISTS $(DB_DATABASE);" | mysql -u $(DB_USER); fi
	if [ "$(CONFIG_TYPE)" = "CI" ]; then echo "CREATE DATABASE IF NOT EXISTS $(DB_DATABASE);" | mysql -u $(DB_USER); fi
	touch $(VENV_LOCATION)/.db


venv: $(VENV_LOCATION)
$(VENV_LOCATION): requirements.txt
	echo $(DB_DATABASE_DRIVER)
	test -d $(VENV_LOCATION) || virtualenv $(VENV_LOCATION) -p $(PYTHON_BINARY)
	. $(VENV_ACTIVATE); pip install -r requirements.txt
	if [ "$(DB_DATABASE_DRIVER)" = "mysql+pymysql" ]; then . $(VENV_ACTIVATE); pip install -r 'requirements-mysql.txt'; fi
	touch $(VENV_LOCATION)
