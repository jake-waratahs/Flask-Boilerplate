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
import config
app.config_class = config.get_config()
app.config.from_object(app.config_class)

# Initialise the boilerplate and do Configuration Magic.
Boilerplate(app)

api = restful.Api(app)
db = SQLAlchemy(app)

# Import everything so the auto-reloader works.
import Application.views as views
import models
import Application.api as api

db.register_base(models.Base)
db.create_all()

# Setup Flask-Security
app.user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
security = Security(app, app.user_datastore)
mail = Mail(app)

# Lib Setup
from Application.lib.setup import Setup
from Application.lib.uploads import Uploads
Setup(app, db)
Uploads(app)
