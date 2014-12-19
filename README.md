Flask Boilerplate (Python 3)
=================

### © Nick Whyte 2014. TwoPi Code

[![build status](http://ci.nickwhyte.com/projects/2/status.png?ref=master)](http://ci.nickwhyte.com/projects/2?ref=master)

Getting Started
---------------

#### 1. Install the [pre-requisites][2]

[2]: <#pre-requisites>

#### 2. Clone to the current working directory

```
git clone git@github.com:nickw444/Flask-Boilerplate.git .
```

#### 3. Setup
```
make venv
```
This command will configure a virtual environment and setup all the required prerequisites outlined in the requirements.txt file. 

#### 4. Run
```
make debug
```

Navigate to [http://localhost:8000/](http://localhost:8000/) and poke around at the included examples in this boilerplate.

You are now up and running and ready to start programming with Flask.

When you first run the webapp, an administrator user is created in the database.
(u: admin@localhost, p: admin). You will probably want to change this if you move your app to a production environment. This function is called within `__init__.py`,  `setup.configure_app()` which executes the `lib/setup.py` file.

#### 5. [Configure][3]
You should consider configuring the app further with your settings
[3]: <#configuration>


Going Further
---------------

`./app` has a few extra features:

#### `./app server`
Run the default flask web server, with auto reload by default. See `./app server --help` for usage.

#### `./app meinheld`
Run a meinheld server. Convenient for quick use in production. See `./app meinheld --help` for usage.

#### `./app install`
Install a bower or github javascript package into the /static/vendor folder. See `./app install --help` for further usage.

### Example:
`./app install bootstrap --version 3.3.1 --with-link`

- --with-link -l: 
	Automatically include this package in the WebApp's header (Experimental - Only includes minifies CSS/JS ending in .min.css)
- --version VERSION -v VERSION: 
	Supply a version to use (Github tag or release)



What’s included?
----------------

Everything to get you up and running with flask. Take a peek inside the
`requirements.txt` file to get an idea of what’s included.

-   flask-restful for an extensive API
-   flask-security for login management
-   flask-sqlalchemy for an ORM (Got to save the data somewhere)
-   flask-classy for Views (MVC)
-   flask-uploads for making your life easier with file uploads.
-   flask-babel for easier translations and easy localisation (Timezones are
    hard)
-   flask-wtforms for easy user input
-	Meinheld web server


Also included are some jinja filters to make your life easier. use `local_date`
or `local_date_time` to correctly format a python datetime object to the locale
chosen in the configuration. Extend this further by using babel’s functionality
for locale switching on a per user basis.

Why should I use this?
----------------------

I’ve developed full time in flask for 6 months now. The collection of packages
bundled with this boilerplate (or rather, listed, available for download)
(Makefile does this), represents a selection of packages I have found extremely
helpful when getting an app up and running as quick as possible.

By using this boilerplate, you should be able to get a functional MVC app within
30 minutes (provided you’ve played with flask before and understand MVC). I have
included examples for most of the libraries included and will bring many more in
the future.

Everything is nicely wrapped into an easy installation via a Makefile which
simplifies the process of setting up a virtual environment and keeps your local
python conflict free and happy :)

Full Makefile Usage
-------------------
Although the app wrapper is very convenient, I am also using a Makefile wrapper.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
make debug [ARGS='[-p 8000]|[--port 8000]']
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start the development environment. You can send further command line arguments
to the python target by supplying them via the `ARGS` parameter.

#### `make test`
Runs tests on the target.


#### `make clean`
Cleans the target. Drops the active database. (or deletes if you’re using
SQLite)

#### `make regenerate`
Regenerate imports for models and recompress/compile CSS.

#### `make uninstall`
Remove the virtual environment and clean the target


Configuration
----------------------

You can find the configuration files within
`WebApp/Application/config/__init__.py`.

You can override how configuration is chosen by editing the `get_config`
function.


Getting Started with MySQL
--------------------------

So, you’re sick of sqlite? No worries!

This guide assume you already have an existing MySQL backend installed. 

Open a MYSQL console using a user that has root privileges

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
mysql -u<user> -p<your_password>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure MySQL for a development user account

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- Create the user account 
CREATE USER 'dev'@'localhost'; 
-- Grant Privs for the dev account 
GRANT ALL PRIVILEGES ON `dev%`.* TO 'dev'@'localhost'; 
-- Exit Mysql 
EXIT;
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set Environment Variable for MYSQL Development (The Dev Environment uses this to
determine what you want to run)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo "export MYSQL_DEV='TRUE'" >> ~/.bashrc 
echo "export MYSQL_DEV='TRUE'" >> ~/.zshrc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Close your terminal, and re-open. You need to reload the environment variables.

Add `mysql-python` to your `requirements.txt` file.

Then execute `make clean`, `make venv` then `make debug`.

How about some Continuous Integration
-------------------------------------

Want to run this on your CI Server? Configure your CI server to build using `make test`

By default the MySQL driver is selected for CI. Your CI Server needs to have the
environment variable of `BUILD_ID` or `CI_BUILD_ID` to have the CI Configuration
chosen automatically, however, this can be overriden by following the setup in
[Advanced Configuration][1].

[1]: <#configuration>

#### Setup MySQL on your CI Server

Open a MYSQL console using a user that has root privileges

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
mysql -u<user> -p<your_password>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure MySQL for a CI user account

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- Create the user account 
CREATE USER 'ci'@'localhost'; 
-- Grant Privs for the dev account 
GRANT ALL PRIVILEGES ON `ci%`.* TO 'ci'@'localhost'; 
-- Exit Mysql 
EXIT;
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Be sure to add `mysql-python` to your `requirements.txt` file as the CI Server needs a driver to communicate with the SQL Server.

