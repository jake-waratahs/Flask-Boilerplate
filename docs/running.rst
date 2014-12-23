Running Flask-Boilerplate Skeleton
==================================================


About ./app
##################################################

``./app`` is actually a very simple program. The main magic lies within ``flask-boilerplate-buildutils``. 

.. literalinclude:: ../app
    :language: python

When ``./app`` is run, it first performs ``patch_cwd``. This helper function within flask-boilerplate-buildutils changes the subprocess's working directory to allow the app to be run no matter what working directory you are in. 

Following, it gets your configuration from the ``config`` module. It then builds the dependencies for the selected config. Such dependencies include setting up the virtual environment for the first time, intitialising the database, or regenerating and minifying css from less.

Next, ``run_app()`` is invoked. This tells your system to run your webapp. ``run_app()`` takes advantage of the ``run.py`` file and any other ``*.py`` files in the root directory of your webapp. 

Usage:
***********************


./app PYFILE ARG1 ARG2 ARG3 ARG4 ARG5 ARGN
    :PYFILE:    The name of a python file in the root directory. ie, <PYFILE>.py
    :ARG1 to ARGN: Arguments to be passed to PYFILE.

By default, ``./app`` will execute the ``run.py`` file. Hence you can omit `PYFILE` if you wish to only run the ``run.py`` file.  *For example:*
 
*./app run.py ARG1 ARG2* is the same as *./app ARG1 ARG2*



About run.py
##################################################

This is the supplied runfile for the app. It makes use of the ``flask-boilerplate-utils.commands`` package to provide abstracted application execution.

.. literalinclude:: ../run.py
    :language: python


Usage
**************************

**usage ./app run [-?] {server,import,meinheld,install}**

*positional arguments:*

    :server:              Run the Flask Builtin Server (Not for production)
    :meinheld:            Run a Web Server for Hosting using meinheld.
    :install:             Install a CSS/JS package listed on bower OR A package
                        from a github repository


Extending
**************************

MainManager returns a flask-script manager object. You can override this and write your own flask-script commands.

If you wish to not override the entire manager, you can just make new BaseCommands:

After the ``manager=`` line, add your new classes:

.. code-block:: python

    from flask_boilerplate_utils.commands import BaseCommand
    from flask.ext.script import Option

    Class MyNewCommand(BaseCommand):
        option_list = (
            Option('--hostname', '-h', dest='hostname', default='0.0.0.0', type=str),
        ) + BaseCommand.option_list

        def run(self, hostname):
            # don't do anything fancy, just print the given hostname
            print(hostname)

    manager.add_command('commandname', MyNewCommand(app))


About test.py
##################################################

This is the supplied test file for the app. Unlike run.py, test.py does not make use of the boilerplate libraries. It simply is invoked to perform tests on the application. 

For more details about tests, see :doc:`writing_tests`


Usage
**************************

**usage: ./app test [-h] [-v] [-q] [-f] [-c] [-b] [tests [tests ...]]**

*positional arguments:*
  :tests:           a list of any number of test modules, classes and test
                  methods.

*optional arguments:*
  -h, --help      show this help message and exit
  -v, --verbose   Verbose output
  -q, --quiet     Quiet output
  -f, --failfast  Stop on first fail or error
  -c, --catch     Catch ctrl-C and display results so far
  -b, --buffer    Buffer stdout and stderr during tests

*Examples:*

  ./app test                           - run default set of tests

  ./app test MyTestSuite               - run suite 'MyTestSuite'

  ./app test MyTestCase.testSomething  - run MyTestCase.testSomething

  ./app test MyTestCase                - run all 'test*' test methods
                                       in MyTestCase



