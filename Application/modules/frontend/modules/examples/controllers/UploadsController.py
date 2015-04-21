from flask.ext.classy import FlaskView, route
from flask import render_template
from flask.ext import menu


class UploadsController(FlaskView):
    route_base = '/uploads'

    @menu.classy_menu_item('frontend.examples.uploads', 'File Uploads', order=3)
    def index(self):
        return render_template('frontend.examples/index.html', is_form=True)

