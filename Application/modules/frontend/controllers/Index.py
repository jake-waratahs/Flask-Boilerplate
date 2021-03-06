from flask.ext.classy import FlaskView, route
from flask import render_template, url_for, redirect
from flask.ext import menu

class Index(FlaskView):
    route_base = '/'

    @menu.classy_menu_item('frontend.account', 'Home', order=0)
    def index(self):
        return render_template('frontend/index.html', is_form=True)


    def generalize(self):
        """
        Provide a HTTP endpoint to generalize this boilerplate. This method 
        will remove all flask-boilerplate examples and clean up the boilerplate
        ready for development of your app.

        TODO
        """
