from flask import Flask
# Get flask Resful for the API usage
from flask.ext import restful
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, login_required
from flask.ext.security.utils import encrypt_password
from flask_mail import Mail



# -------------------
#  Initial App Setup
# -------------------

app = Flask(__name__)

# Configure the app.
import config as config

app.config.from_object(config.get_config())


api = restful.Api(app)
db = SQLAlchemy(app)


# Import everything so the auto-reloader works.
from Application.views import *
from Application.models import *
from Application.api import *

from Application.models import (
    User, 
    Role
)

# Setup Flask-Security



user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

db.create_all()

mail = Mail(app)


def setup():
    with app.app_context():
        db.create_all()

        if (len(User.query.filter_by(email='admin@localhost').all()) == 0):
            if len(Role.query.filter_by(name='admin').all()) == 0:
                # No user exists, create one.
                user_datastore.create_role(name="admin", description="Admin Users")
                user_datastore.create_user(email='admin@localhost', password=encrypt_password('admin'))
                db.session.commit()

                user = user_datastore.find_user(email='admin@localhost')
                role = user_datastore.find_role('admin')
                user_datastore.add_role_to_user(user, role)

                db.session.commit()


setup()
    

# ---------------------
# Jinja Filters
# ---------------------
from lib.jinja_filters import insert_filters
insert_filters(app)


# ---------------------
# Setup App Debug Emails so we can monitor exceptions
# ---------------------
ADMINS = ['admin@localhost']
if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    mail_handler = SMTPHandler('127.0.0.1', 'server-error@localhost.com', ADMINS, 'Application Failed')
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)


