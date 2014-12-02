from flask import Flask
# Get flask Resful for the API usage
from flask.ext import restful
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, login_required
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

from Application.lib import setup
setup()
    

# ---------------------
# Jinja Filters
# ---------------------
from lib.jinja_filters import insert_filters
insert_filters(app)


# ---------------------
# Setup App Debug via Sentry
# ---------------------
if not app.debug:
    from raven.contrib.flask import Sentry
    sentry = Sentry(APP)


