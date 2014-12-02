# Determine the DB Driver
CONFIG_TYPE=`python Application/config`
DB_DATABASE=`python Application/config -k _CONFIG_DB_NAME`
DB_USER=`python Application/config -k _CONFIG_DB_USER`
DB_BASE=`python Application/config -k _CONFIG_DB_BASE`

RUN_SCRIPT='run.py'
RUN_TEST_SCRIPT='test.py'

VENV_LOCATION=.venv
VENV_ACTIVATE="$(VENV_LOCATION)/bin/activate"
REQUIREMENTS="requirements.txt"

all: debug

debug: venv regenerate db configure
	. $(VENV_ACTIVATE); python $(RUN_SCRIPT) $(ARGS)

test: venv regenerate db configure
	. $(VENV_ACTIVATE); python $(RUN_TEST_SCRIPT) $(ARGS)

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

reconfigure: 
	. $(VENV_ACTIVATE); ./util/configure
	touch $(VENV_LOCATION)/.configure



# A little bit of hack
configure:  venv $(VENV_LOCATION)/.configure
$(VENV_LOCATION)/.configure:	
	. $(VENV_ACTIVATE); ./util/configure
	touch $(VENV_LOCATION)/.configure

db: venv $(VENV_LOCATION)/.db
$(VENV_LOCATION)/.db:
	if [ "$(CONFIG_TYPE)" = "MySQLStd" ]; then echo "CREATE DATABASE IF NOT EXISTS $(DB_DATABASE);" | mysql -u $(DB_USER); fi
	if [ "$(CONFIG_TYPE)" = "CI" ]; then echo "CREATE DATABASE IF NOT EXISTS $(DB_DATABASE);" | mysql -u $(DB_USER); fi
	touch $(VENV_LOCATION)/.db

venv: $(VENV_LOCATION)
$(VENV_LOCATION): requirements.txt
	test -d $(VENV_LOCATION) || virtualenv $(VENV_LOCATION)
	. $(VENV_ACTIVATE); pip install -r $(REQUIREMENTS)
	touch $(VENV_LOCATION)