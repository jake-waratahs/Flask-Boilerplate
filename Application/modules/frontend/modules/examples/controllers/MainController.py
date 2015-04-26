from flask.ext.classy import FlaskView, route
from flask import render_template
from flask.ext import menu



class MainController(FlaskView):
    route_base = '/'

    @menu.classy_menu_item('frontend.examples', 'Examples', order=1)
    @menu.classy_menu_item('frontend.examples.all', 'All Examples', order=0)
    def index(self):
        return render_template('frontend.examples/index.html', is_form=True)
