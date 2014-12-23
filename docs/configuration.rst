Configuration
==================================================

The boilerplate comes with some configuration already set.  Visit the ``./config/__init__.py`` file to see what the skeleton has to offer.

Included are classes: 

    - Production
    - Development
    - MySQLStd
    - CI

You can override or subclass these provided classes.

How does config get chosen?
#########################################

The ``get_config()`` function returns a class for the desired configuration. By default, flask-boilerplate-buildutils handles this. You can override this behaviour by changing the function.

**Default Behavior**

Flask Boilerplate Build Utils will first check the command line arguments for ``'-c CONFIGNAME'`` or ``'--c CONFIGNAME'`` and use the config name from there. If no '-c' flag is set, it will check the environment to determine if you have the ``"FLASK_CONFIG"`` environment variable set. If it is set, it will set the config class string to the value of this variable. 

Once we have a config class name, the module looks up the class, and returns it as a Class, ready for usage around the app. 


Develop Using MySQL
#########################################

So, you’re sick of sqlite? No worries! This guide assume you already have an existing MySQL backend installed. Open a MYSQL console using a user that has root privileges

.. code-block:: mysql

    mysql -u <USER> -p<PASSWORD>

    -- Create the user account 
    CREATE USER 'dev'@'localhost'; 
    -- Grant Privs for the dev account 
    GRANT ALL PRIVILEGES ON `dev%`.* TO 'dev'@'localhost'; 
    -- Exit Mysql 
    EXIT;

Set Environment Variable for MYSQL Development (The Dev Environment uses this to
determine what you want to run)

.. code-block:: bash

    echo "export FLASK_CONFIG=MySQLStd" >> ~/.bashrc 
    echo "export FLASK_CONFIG=MySQLStd" >> ~/.zshrc

Close your terminal, and re-open. You need to reload the environment variables.

The app will now execute in mysql development mode.

Continuous Integration
#########################################


Want to run this on your CI Server? By default the MySQL driver is selected for CI. 

**Setup MySQL on your CI Server**

Open a MYSQL console using a user that has root privileges

.. code-block:: mysql

    mysql -u<user> -p<your_password>

    -- Create the user account 
    CREATE USER 'ci'@'localhost'; 
    -- Grant Privs for the ci account 
    GRANT ALL PRIVILEGES ON `ci%`.* TO 'ci'@'localhost'; 
    -- Exit Mysql 
    EXIT;

**Add a CI Build Script** on your CI Server:

.. code-block:: bash

    export FLASK_CONFIG=CI
    ./app test



