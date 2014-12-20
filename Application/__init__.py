from flask import Flask
# Get flask Resful for the API usage
from flask.ext import restful
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore
from flask_mail import Mail
from flask_boilerplate_utils import Boilerplate

#  Initial App Setup
app = Flask(__name__)

# Configure the app.
import Application.config as config
app.config.from_object(config.get_config())

# Initialise the boilerplate
Boilerplate(app)

api = restful.Api(app)
db = SQLAlchemy(app)

# Import everything so the auto-reloader works.
import Application.views as views
import Application.models as models
import Application.api as api

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
security = Security(app, user_datastore)
db.create_all()
mail = Mail(app)

# Lib Setup
import Application.lib.setup as setup
import Application.lib.uploads as uploads

setup.configure_app()
uploads.configure_uploads(app)
