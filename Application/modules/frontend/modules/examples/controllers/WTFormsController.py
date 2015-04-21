from flask.ext.classy import FlaskView, route
from flask import render_template
from flask.ext import menu


class WTFormsController(FlaskView):
    route_base = '/wtforms/'

    @menu.classy_menu_item('frontend.examples.forms', 'WTForms', order=14)
    def index(self):
        return render_template('frontend.examples/index.html', is_form=True)

