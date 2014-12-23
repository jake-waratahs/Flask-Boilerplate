Flask Boilerplate
================================================

Get started with flask MVC in 30 minutes. This boilerplate skeleton includes everything to get you up and running with flask. The collection of packages bundled with this boilerplate represents a selection of packages I have found extremely helpful when getting an app up and running as quick as possible.

This module is part of the flask-boilerplate project.

- `flask-boilerplate <https://github.com/nickw444/Flask-Boilerplate>`_
- `flask-boilerplate-buildutils <https://github.com/nickw444/flask-boilerplate-buildutils>`_
- `flask-boilerplate-utils <https://github.com/nickw444/flask-boilerplate-utils>`_
- `maketools <https://github.com/nickw444/python-maketools>`_


Features
*******************
- Makes use of `virtual environments <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_ transparently, so you never need to worry about source ./venv/bin/activate again or any dependency errors.
- Abstracted boilerplate utilities in flask-boilerplate-buildutils and flask-boilerplate-utils  - you can always upgrade to the latest and greatest.
- Instantly ready for deployment. Never mess around with gunicorn again. See :doc:`deployment` for more details on how to deploy using supervisor and nginx.


Full usage available at `read the docs <http://flask-boilerplate.readthedocs.org/en/latest/>`_

What's Included
*******************

Everything to get you up and running with flask. Take a peek inside the
``Application/requirements.txt`` file to get an idea of what’s included.

:flask-restful:         for an extensive API
:flask-security:        for login management
:sqlalchemy:      for an ORM (Got to save the data somewhere)
:flask-classy:          for Views (MVC)
:flask-uploads:         for making your life easier with file uploads.
:flask-babel:           for easier translations and easy localisation (Timezones are hard)
:flask-wtforms:         for easy user input
:Meinheld:   for hosting on production in a single click


Prerequisites
*********************************
- You have Python 3 Installed
- You have Pip 3 Installed through Python 3.
