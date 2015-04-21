from flask.ext.classy import FlaskView, route
from flask import render_template
from flask.ext import menu



class SecurityController(FlaskView):
    route_base = '/security'

    @menu.classy_menu_item('frontend.examples.security', 'Security', order=3)
    def index(self):
        return render_template('frontend.examples/index.html', is_form=True)
