from flask.ext.classy import FlaskView, route
from flask import render_template
from flask.ext import menu

class Index(FlaskView):
    route_base = '/'

    @menu.classy_menu_item('frontend.learn_flask', 'Learn Flask', order=3)
    def index(self):
        return render_template('learn_flask/index.html', is_form=True)