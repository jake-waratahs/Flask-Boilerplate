.. Flask Boilerplate documentation master file, created by
   sphinx-quickstart on Wed Dec 24 00:04:11 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. include:: ../README.rst

Getting Started
******************************************

1. Get the skeleton project
##########################################

**Using Git**

Open a bash/zsh console.

.. code-block:: bash
    
    mkdir -p ~/projects/my_new_project/
    cd ~/projects/my_new_project/
    git clone -b release git@github.com:nickw444/Flask-Boilerplate.git .
    rm -rf .git

You will probably wish to change where you install the project to by changing
the path given to mkdir and cd. 


**OR: Using your GUI**

Download the latest `tarball <https://github.com/user/repository/tarball/release/>`_ or 
`zipball <https://github.com/user/repository/zipball/zipball/>`_ from github and extract 
it where you want to start building your app.


Open a terminal session and execute:

.. code-block:: bash
    
    cd /path/to/expanded/folder



2. Install project dependencies
##########################################

Ensure you are cd'd into the directory of your project (You should be if you
followed the above steps correctly).

.. code-block:: bash
    
    pip3 install -r requirements.txt

This will install the required packages. These include:

.. include:: ../requirements.txt
    
3. Test it out
##########################################

.. code-block:: bash
    
    ./app

This invokes the flask-boilerplate executor. During the first run it will 
perform some build commands which setup and configure a virtual environment
in the folder ./.venv/. The `./app` command always invoke your app via the
virtualenv so there is never any reason for you to perform any `source` commands
in your shell. See more about the ./app command in :doc:`running`

4. Developing with Flask-Boilerplate
##########################################
See the :doc:`development` to learn how to structure your project using the
boilerplate.

See the :doc:`configuration` to learn how to to correctly configure your project.


.. toctree::
   :maxdepth: 2
   :hidden:

   index
   running
   configuration
   develop_mysql
   develop_ci
   development
   deployment
