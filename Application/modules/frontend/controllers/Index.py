from flask.ext.classy import FlaskView, route
from flask import render_template
from flask.ext import menu

class Index(FlaskView):
    route_base = '/'

    @menu.classy_menu_item('frontend.account', 'My Account', order=0)
    def index(self, **kwargs):
        return render_template('frontend/index.html', is_form=True)


    @menu.classy_menu_item('frontend.account2', 'My Account2', order=1, visible_when=lambda: False)
    def index2(self, **kwargs):
        return render_template('frontend/index.html', is_form=True)


