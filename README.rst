Flask Boilerplate
=================

© Nick Whyte 2014. TwoPi Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|build status|

Getting Started
---------------

1. Install the `pre-requisites <#requirements>`__
'''''''''''''''''''''''''''''''''''''''''''''''''

2. Install Foiler/Flask Boilerplate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Foiler is the helper script for the boilerplate. It takes care of
initialising, configuring, hosting and managing your flask application.

To install foiler:

::

    pip install flask-boilerplate

3. Ready. Set. Go!
~~~~~~~~~~~~~~~~~~

Use ``foiler`` to make a new flask instance. Go to the place you wish to
set up and type:

::

    foiler init

Foiler will ask you a few q uestions and copy all the required files
into your project to get you started. Next, you will need to configure
the Application. Type:

::

    foiler configure

Foiler will ask you values for some variables in it's configuration. If
you are unsure, hit the return key to use the default value.

You can view all the configuration directives in the `advanced
configuration <#advanced-configuration>`__ section.

When you're all configured, you will be ready to start up the server and
navigate to the web page. Type:

::

    foiler server

Running this command for the first time will take a little bit of extra
time. It needs to download the pre-requisites for the project. Once
started up, you will see the message

::

     * Running on http://0.0.0.0:8000/
     * Restarting with reloader

Navigate to http://localhost:8000/ and poke around at the included
examples in this boilerplate.

You are now up and running and ready to start programming with Flask.

Foiler Features
---------------

Foiler has a multitude of command line options.

Foiler should generally work no matter what child directory you are
within. As long as somewhere up the parent chain, foiler will be able to
perform operations on your application.

::

    init

Initialises a new flask boilerplate in the current working directory.

::

    configure

Configure/Reconfigure the app in the current working directory.

::

    server

Spawn a flask server for the app in the working directory. (For
Development Only) ##### Additional Parameters - --hostname HOSTNAME -h
HOSTNAME: Provide a binding hostname for the server - --port PORT -p
PORT: Provide a binding port for the server.

::

    test

Run the tests from the testfile in the project directory.

::

    install-framework

Install a CSS/JS package listed on bower OR a package from a github
repository in the format of user/repo. ##### Additional Parameters -
--with-link -l: Automatically include this package in the WebApp's
header (Experimental - Only includes minifies CSS/JS ending in .min.css)
- --version VERSION -v VERSION: Supply a version to use (Github tag or
release)

What’s included?
----------------

Everything to get you up and running with flask. Take a peek inside the
``requirements.txt`` file to get an idea of what’s included.

-  flask-restful for an extensive API
-  flask-security for login management
-  flask-sqlalchemy for an ORM (Got to save the data somewhere)
-  flask-classy for Views (MVC)
-  flask-uploads for making your life easier with file uploads.
-  flask-babel for easier translations and easy localisation (Timezones
   are hard)
-  flask-wtforms for easy user input

When you first run the webapp, an administrator user is created in the
database. (u: admin@localhost, p: admin). You will probably want to
change this if you move your app to a production environment.

Also included are some jinja filters to make your life easier. use
``local_date`` or ``local_date_time`` to correctly format a python
datetime object to the locale chosen in the configuration. Extend this
further by using babel’s functionality for locale switching on a per
user basis.

Requirements
------------

-  `Homebrew (If you're on OSX) <http://brew.sh/>`__
-  Node JS Install via (OSX): ``brew install node`` Install via (Linux):
   ``sudo apt-get install nodejs``
-  Less CSS Compiler Install via: ``npm install -g less``
-  Homebrew Python 2 (If you are not already using it) Install Via
   ``brew install python; brew link python;``
-  Python Virtualenv Install via: ``pip install virtualenv``
-  Flask Install Via ``pip install flask``
-  Flask-Script Install Via ``pip install flask-script``

Why should I use this?
----------------------

I’ve developed full time in flask for 6 months now. The collection of
packages bundled with this boilerplate (or rather, listed, available for
download) (Makefile does this), represents a selection of packages I
have found extremely helpful when getting an app up and running as quick
as possible.

By using this boilerplate, you should be able to get a functional MVC
app within 30 minutes (provided you’ve played with flask before and
understand MVC). I have included examples for most of the libraries
included and will bring many more in the future.

Everything is nicely wrapped into an easy installation via a Makefile
which simplifies the process of setting up a virtual environment and
keeps your local python conflict free and happy :)

Full Makefile Usage
-------------------

Although the foiler wrapper is very convenient, I am using a Makefile
wrapper which means you don't need to have foiler installed on every
machine you wish to develop on. The following docs outline what the
makefile can do for you.

::

    make [ARGS='[-p 8000]|[--port 8000]']

Start the development environment. You can send further command line
arguments to the python target by supplying them via the ``ARGS``
parameter.

::

    make test

Runs tests on the target.

::

    make clean

Cleans the target. Drops the active database. (or deletes if you’re
using SQLite)

::

    make regenerate

Regenerate imports for models and recompress/compile CSS.

::

    make uninstall

Remove the virtual environment and clean the target

Advanced Configuration
----------------------

You can find the configuration files within
``WebApp/Application/config/__init__.py``.

You can override how configuration is chosen by editing the
``get_config`` function.

Configuration made during the ``make reconfigure`` and
``make configure`` build tasks can be edited in the
``WebApp/Application/config/variables.py`` file. If you wish to start
fresh, delete this file and re-run ``make configure``.

Getting Started with MySQL
--------------------------

So, you’re sick of sqlite? No worries!

This guide assume you already have an existing MySQL backend installed.

Open a MYSQL console using a user that has root privileges

::

    mysql -u<user> -p<your_password>

Configure MySQL for a development user account

::

    -- Create the user account 
    CREATE USER 'dev'@'localhost'; 
    -- Grant Privs for the dev account 
    GRANT ALL PRIVILEGES ON `dev%`.* TO 'dev'@'localhost'; 
    -- Exit Mysql 
    EXIT;

Set Environment Variable for MYSQL Development (The Dev Environment uses
this to determine what you want to run)

::

    echo "export MYSQL_DEV='TRUE'" >> ~/.bashrc 
    echo "export MYSQL_DEV='TRUE'" >> ~/.zshrc

Close your terminal, and re-open. You need to reload the environment
variables.

Add ``mysql-python`` to your ``requirements.txt`` file.

Then execute ``make clean``, ``make venv`` then ``make debug``.

How about some Continuous Integration
-------------------------------------

Want to run this on your CI Server? Configure your CI server to build
using ``make test``

By default the MySQL driver is selected for CI. Your CI Server needs to
have the environment variable of ``BUILD_ID`` or ``CI_BUILD_ID`` to have
the CI Configuration chosen automatically, however, this can be
overriden by following the setup in `Advanced
Configuration <#advanced-configuration>`__.

Setup MySQL on your CI Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open a MYSQL console using a user that has root privileges

::

    mysql -u<user> -p<your_password>

Configure MySQL for a CI user account

::

    -- Create the user account 
    CREATE USER 'ci'@'localhost'; 
    -- Grant Privs for the dev account 
    GRANT ALL PRIVILEGES ON `ci%`.* TO 'ci'@'localhost'; 
    -- Exit Mysql 
    EXIT;

Be sure to add ``mysql-python`` to your ``requirements.txt`` file as the
CI Server needs a driver to communicate with the SQL Server.

 What’s Up Next (TODO)?
-----------------------

-  Write a utility to automatically migrate the models
-  Move away from makefiles using the above utility.
-  Pip/Pypi package 

.. |build status| image:: http://ci.nickwhyte.com/projects/2/status.png?ref=master
   :target: http://ci.nickwhyte.com/projects/2?ref=master
