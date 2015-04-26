"""
A Module to clean up the boilerplate and delete everything. 
"""

from flask import Blueprint


cleanup = Blueprint('frontend.cleanup', __name__, template_folder="templates", 
    static_folder="static")

from flask.ext.classy import FlaskView, route
from flask.ext import menu
from flask import render_template, request, redirect


class Cleanup(FlaskView):
    route_base = '/'

    @menu.classy_menu_item('frontend.cleanup', 'Cleanup', order=4)
    def index(self):

        return render_template('frontend.cleanup/index.html')

Cleanup.register(cleanup)
menu.register_flaskview(cleanup, Cleanup)
