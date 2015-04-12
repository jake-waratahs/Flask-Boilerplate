from flask.ext.classy import FlaskView, route
from flask import render_template, url_for, redirect
from flask.ext import menu

class Index(FlaskView):
    route_base = '/'

    @menu.classy_menu_item('frontend.account', 'Index', order=0)
    def index(self):
        return render_template('frontend/index.html', is_form=True)


    @menu.classy_menu_item('frontend.examples', 'Examples', order=1)
    @menu.classy_menu_item('frontend.examples.all', 'All Examples', order=0)
    def examples_home(self):
        return render_template('frontend/examples_home.html', is_form=True)


    @menu.classy_menu_item('frontend.examples.submodule', 'Submodule', order=1) 
    def submodule_example(self):
        return redirect(url_for('.submodule.Index:index', id=1))


    @menu.classy_menu_item('frontend.submodule.right.settings', 'Settings', order=0)
    def settings(self, id):
        return render_template('submodule/index.html', is_form=True)
