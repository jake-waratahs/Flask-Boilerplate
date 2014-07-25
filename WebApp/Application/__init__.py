from flask import Flask
# Get flask Resful for the API usage
from flask.ext import restful
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from flask.ext.security.utils import encrypt_password
from flask_mail import Mail



# -------------------
#  Initial App Setup
# -------------------

app = Flask(__name__)

# DB Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datastore.db'
app.config['SECRET_KEY'] = 'lakufy23kiu4yjkhd,asasd2213@#$!@321h@!#1jdg23kuhj3'
app.config['SECURITY_PASSWORD_SALT'] = "912873@!#28974ew987df9as87d2jghj21g3jh2"
# Please don't use plaintext.
app.config['SECURITY_PASSWORD_HASH'] = 'plaintext'

api = restful.Api(app)
db = SQLAlchemy(app)



import Application.views
import Application.api
import Application.models
from Application.models.User import User, Role

# Setup Flask-Security
app.config['SECURITY_RECOVERABLE'] = True
app.config['SECURITY_CHANGEABLE'] = True
app.config['SECURITY_EMAIL_SENDER'] = 'security@localhost'



user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
app.user_datastore = user_datastore

db.create_all()


# Flask Security Email Setup
# After 'Create app'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['SECURITY_UNAUTHORIZED_VIEW'] = '/unauthorised'
mail = Mail(app)


def setup():
    db.create_all()
    if (len(User.query.filter_by(email='root@localhost').all()) == 0):
        # No user exists, create one.
        user_datastore.create_role(name="admin", description="Admin Users")
        user_datastore.create_user(email='root@localhost', password=encrypt_password('toor'))
        db.session.commit()

        user = user_datastore.find_user(email='root@localhost')
        role = user_datastore.find_role('admin')
        result = user_datastore.add_role_to_user(user, role)

        db.session.commit()


# # Create a user to test with
@app.before_first_request
def create_user():
    setup()
    pass
    

# ---------------------
# Setup App Debug Emails so we can monitor exceptions
# ---------------------
ADMINS = ['admin@localhost']
if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    mail_handler = SMTPHandler('127.0.0.1', 'server-error@localhost.com', ADMINS, 'Cladmix Application Failed')
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)


