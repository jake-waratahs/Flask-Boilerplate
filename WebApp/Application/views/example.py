from Application import app
from flask import render_template, Response
from flask.ext.security import login_required, current_user, roles_required
from Application.models import *


# Examples without the use of classy.

@app.route("/protected/")
@login_required
def protected():
	return render_template('index.html')