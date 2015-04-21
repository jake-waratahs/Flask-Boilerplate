from flask.ext.classy import FlaskView, route
from flask import render_template
from flask.ext import menu



class Features(FlaskView):
    route_base = '/'

    @menu.classy_menu_item('frontend.examples.MySQL', 'Developing with MySQL', order=3)
    def mysql(self):
        return render_template('frontend.examples/index.html', is_form=True)

    @menu.classy_menu_item('frontend.examples.running', 'Running', order=3)
    def running(self):
        return render_template('frontend.examples/index.html', is_form=True)

    @menu.classy_menu_item('frontend.examples.models', 'Models', order=3)
    def models(self):
        return render_template('frontend.examples/index.html', is_form=True)

    @menu.classy_menu_item('frontend.examples.helpers', 'Helpers', order=3)
    def helpers(self):
        return render_template('frontend.examples/index.html', is_form=True)


    @menu.classy_menu_item('frontend.examples.env', '.env', order=3)
    def env(self):
        return render_template('frontend.examples/index.html', is_form=True)


    @menu.classy_menu_item('frontend.examples.ci', 'Continuous Integration', order=3)
    def ci(self):
        return render_template('frontend.examples/index.html', is_form=True)


    @menu.classy_menu_item('frontend.examples.submodules', 'Blueprint Submodules', order=3)
    def ci(self):
        return render_template('frontend.examples/index.html', is_form=True)
