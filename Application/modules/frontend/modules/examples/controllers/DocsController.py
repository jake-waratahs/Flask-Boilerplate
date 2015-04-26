from flask.ext.classy import FlaskView, route
from flask import render_template
from flask.ext import menu


class DocsController(FlaskView):
    route_base = '/docs'

    @menu.classy_menu_item('frontend.docs', 'Documentation', order=1)
    @menu.classy_menu_item('frontend.docs.all', 'All Documentation', order=1)
    def index(self):
        return render_template('frontend.examples/docs/index.html')


    @menu.classy_menu_item('frontend.docs.MySQL', 'Developing with MySQL', 
        order=7, description="Drop SQLite, use a real database.")
    def mysql(self):
        return render_template('frontend.examples/docs/mysql.html')

    @menu.classy_menu_item('frontend.docs.running', 'Running & Usage', 
        order=2, description='Learn about <code>run.py</code>.'\
        ' Detailed documentation of command line arguments and how to extend '\
        'to add additional commands.')
    def running(self):
        return render_template('frontend.examples/docs/running.html')
    @menu.classy_menu_item('frontend.docs.env', 'More about .env', order=3,
        description='Learn more about the <code>.env</code> shell script used'\
        ' to activate the virtual environment for the project..')
    def env(self):
        return render_template('frontend.examples/docs/env.html')


    @menu.classy_menu_item('frontend.docs.ci', 'Testing & Continuous Integration', 
        order=4, description='Use the builtin tests directory to run tests on '\
        'your Flask application. Documents how to write tests and how to deploy'\
        ' to a CI server.')
    def ci(self):
        return render_template('frontend.examples/docs/ci.html')


    @menu.classy_menu_item('frontend.docs.configuration', 'Configuration', 
        order=5, description='Set configuration variables for your app. '\
        'Classful configuration depending on the environment the app is '\
        'being run from. ')
    def configuration(self):
        return render_template('frontend.examples/docs/configuration.html')

    @menu.classy_menu_item('frontend.docs.grunt', 'Grunt', 
        order=6, description='Use grunt to manage web dependencies.')
    def grunt(self):
        return render_template('frontend.examples/docs/grunt.html')





