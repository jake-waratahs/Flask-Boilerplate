from Application import app
from flask import render_template, Response
from flask.ext.security import login_required, current_user, roles_required
from Application.models import *
from flask.ext.classy import FlaskView, route

# Classy index example.

class Index(FlaskView):
    route_base = '/'

    def index(self):
        return render_template('index.html')


Index.register(app)
