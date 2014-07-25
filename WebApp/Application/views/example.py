from Application import app
from flask import render_template, Response
from flask.ext.security import login_required, current_user, roles_required
from Application.models import *


@app.route("/")
# @login_required
# @roles_required('admin')
def example():
    return render_template('index.html')


@app.route("/protected/")
@login_required
def protected():
	return render_template('index.html')