from flask.ext.classy import route
from flask import render_template
from flask.ext import menu
from flask_boilerplate_utils import FlaskView

class Index(FlaskView):
    route_base = '/'

    @menu.classy_menu_item('frontend.submodule.left.index', 'Index', order=0)
    def index(self, id):
        return render_template('submodule/index.html', is_form=True)

    @menu.classy_menu_item('frontend.submodule.right.settings', 'Settings', order=0)
    def settings(self, id):
        return render_template('submodule/index.html', is_form=True)

