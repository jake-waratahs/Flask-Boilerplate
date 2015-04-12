from flask.ext.classy import FlaskView, route
from flask import render_template

class Index(FlaskView):
    route_base = '/'

    def index(self, **kwargs):
        return render_template('backend/index.html', is_form=True)