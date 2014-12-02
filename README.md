Flask Boilerplate
=================

### © Nick Whyte 2014. TwoPi Code
[![build status](http://ci.nickwhyte.com/projects/2/status.png?ref=master)](http://ci.nickwhyte.com/projects/2?ref=master)
Getting Started
---------------

Setup the environment

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
make configure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the environment

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
make debug
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

When you first run the webapp, an administrator user is created in the database.
(u: admin\@localhost, p: admin). You will probably want to change this if you
move your app to a production environment.

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

Requirements
------------

-   A Computer

-   Python 2 (Have not tested compatability on Python 3)

-   The requirements and makefiles take care of the rest for you.

Full Makefile Usage
-------------------

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
make configure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This command will configure the development environment. Enter the required
info. Leaving a blank response will use the default value.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
make [ARGS='[-p 8000]|[--port 8000]']
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start the development environment. You can send further command line arguments
to the python target  by supplying them via the `ARGS` parameter.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
make test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Runs tests on the target.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
make clean
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cleans the target. Drops the active database. (or deletes if you’re using
SQLite)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
make regenerate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Regenerate imports for models and recompress/compile CSS.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
make reconfigure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reconfigure the environment.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
make uninstall
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove the virtual environment and clean the target

Advanced Configuration
----------------------

You can find the configuration files within
`WebApp/Application/config/__init__.py`.

You can override how configuration is chosen by editing the `get_config`
function.

Getting Started with MySQL
--------------------------

So, you’re sick of sqlite? No worries!

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
Then execute `make clean` then `make debug`

How about some Continuous Integration
-------------------------------------

Want to run this on your CI Server? Configure your CI server to build the
`./ci.sh`  file. This simply executes `make test`

By default the MySQL driver is selected for CI. Your CI Server needs to have the
environment variable of `BUILD_ID` or `CI_BUILD_ID` to have the CI Configuration
chosen automatically, however, this can be overriden by following the setup in
[Advanced Configuration][1].

[1]: <#advanced-configuration>

#### Setup MySQL on your CI Server

Open a MYSQL console using a user that has root privileges

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
mysql -u<user> -p<your_password>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure MySQL for a development user account

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- Create the user account 
CREATE USER 'ci'@'localhost'; 
-- Grant Privs for the dev account 
GRANT ALL PRIVILEGES ON `ci%`.* TO 'ci'@'localhost'; 
-- Exit Mysql 
EXIT;
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

 
