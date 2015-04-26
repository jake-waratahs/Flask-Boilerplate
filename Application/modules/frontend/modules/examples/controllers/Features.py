from flask.ext.classy import FlaskView, route
from flask import render_template
from flask.ext import menu



class Features(FlaskView):
    route_base = '/'

    @menu.classy_menu_item('frontend.examples.models', 'Models', order=4, 
        description='Add a database schema to your project. Includes sample '\
        'models and how to use Raw SQLAlchemyin your flask app.')
    def models(self):
        return render_template('frontend.examples/models.html')

    @menu.classy_menu_item('frontend.examples.views', 'Views', order=4, 
        description='Use Flask-Classy to provide classful views in your app.')
    def views(self):
        return render_template('frontend.examples/views.html')

    @menu.classy_menu_item('frontend.examples.helpers', 'Helpers', order=11, 
        description='Learn more about the helper filters, globals and classes '\
        'the Flask Boilerplate brings to your Flask project.')
    def helpers(self):
        return render_template('frontend.examples/helpers.html')

    @menu.classy_menu_item('frontend.examples.submodules', 'Blueprint Submodules', 
        order=12, description='Nestable submodules using Flask Blueprints. '\
        'Write completely modular applications with pluggable sections.')
    def submodules(self):
        return render_template('frontend.examples/submodules.html')