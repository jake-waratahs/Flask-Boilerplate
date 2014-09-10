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

# DB Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datastore.db'
app.config['SECRET_KEY'] = 'Change Me'
app.config['SECURITY_PASSWORD_SALT'] = "Change Me"
# Please don't use plaintext.
app.config['SECURITY_PASSWORD_HASH'] = 'plaintext'

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
app.config['SECURITY_RECOVERABLE'] = True
app.config['SECURITY_CHANGEABLE'] = True
app.config['SECURITY_EMAIL_SENDER'] = 'security@localhost'



user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
app.user_datastore = user_datastore

db.create_all()


# Flask Security Email Setup

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['SECURITY_UNAUTHORIZED_VIEW'] = '/unauthorised'
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


