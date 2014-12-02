Flask Boilerplate
-----------------

### Nick Whyte - TwoPi Code © 2014

 

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

Start the development environment.

You can send further command line arguments to the python target  by supplying
them via the `ARGS` parameter.

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
make test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Runs tests on the target.

You can send further command line arguments to the python target  by supplying
them via the \`ARGS\` parameter.

 

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

 

Getting Started with MySQL
--------------------------

So, you’re sick of sqlite? No worries!

 

 
