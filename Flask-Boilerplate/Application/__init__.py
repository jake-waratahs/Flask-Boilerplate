from flask import Flask
# Get flask Resful for the API usage
from flask.ext import restful
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore
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
import Application.views as views
import Application.models as models
import Application.api as api

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
security = Security(app, user_datastore)
db.create_all()
mail = Mail(app)

# WTforms/CSRF Protection
from flask_wtf.csrf import CsrfProtect
csrf = CsrfProtect(app)

# Lib Setup
import Application.lib.setup as setup
import Application.lib.uploads as uploads
import Application.lib.jinja_filters as jinja_filters
setup.configure_app()
uploads.configure_uploads(app)
jinja_filters.configure_filters(app)

# Setup App Debug via Sentry (When in production)
if not app.debug:
    from raven.contrib.flask import Sentry
    sentry = Sentry(APP)



