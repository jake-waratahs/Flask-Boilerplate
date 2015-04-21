from flask.ext.classy import FlaskView, route
from flask import render_template
from flask.ext import menu



class Features(FlaskView):
    route_base = '/'

    @menu.classy_menu_item('frontend.examples.MySQL', 'Developing with MySQL', order=7)
    def mysql(self):
        return render_template('frontend.examples/mysql.html', is_form=True)

    @menu.classy_menu_item('frontend.examples.running', 'Running & Usage', order=1)
    def running(self):
        return render_template('frontend.examples/running.html', is_form=True)

    @menu.classy_menu_item('frontend.examples.models', 'Models', order=4)
    def models(self):
        return render_template('frontend.examples/models.html', is_form=True)

    @menu.classy_menu_item('frontend.examples.helpers', 'Helpers', order=11)
    def helpers(self):
        return render_template('frontend.examples/helpers.html', is_form=True)


    @menu.classy_menu_item('frontend.examples.env', 'More about .env', order=3)
    def env(self):
        return render_template('frontend.examples/env.html', is_form=True)


    @menu.classy_menu_item('frontend.examples.ci', 'Continuous Integration', order=9)
    def ci(self):
        return render_template('frontend.examples/ci.html', is_form=True)


    @menu.classy_menu_item('frontend.examples.submodules', 'Blueprint Submodules', order=12)
    def submodules(self):
        return render_template('frontend.examples/submodules.html', is_form=True)

    @menu.classy_menu_item('frontend.examples.configuration', 'Configuration', order=5)
    def configuration(self):
        return render_template('frontend.examples/configuration.html', is_form=True)
