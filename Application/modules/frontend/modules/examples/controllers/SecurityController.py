from flask.ext.classy import FlaskView, route
from flask import render_template
from flask.ext import menu
from flask.ext.security import login_required


class SecurityController(FlaskView):
    route_base = '/security'

    @menu.classy_menu_item('frontend.examples.security', 'Security', order=12, 
        description='Use Flask-Security to provide a login/logout mechanism '\
        'and user groups/roles.')
    def index(self):
        return render_template('frontend.examples/security/index.html')


    @login_required
    def secure_view(self):
        return render_template('frontend.examples/security/secure.html')
        