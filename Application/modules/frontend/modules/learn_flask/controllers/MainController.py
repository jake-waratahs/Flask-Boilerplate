from flask.ext.classy import FlaskView, route
from flask import render_template
from flask.ext import menu



class MainController(FlaskView):
    route_base = '/'

    @menu.classy_menu_item('frontend.learn_flask', 'Learn Flask', order=3)
    @menu.classy_menu_item('frontend.learn_flask.learn_flask', 'Learn Flask', order=0)
    def index(self):
        return render_template('learn_flask/index.html')

    @menu.classy_menu_item('frontend.learn_flask.what_is_flask', 'What Is Flask', order=1)
    def what_is_flask(self):
        return render_template('learn_flask/what-is-flask.html')


    @menu.classy_menu_item('frontend.learn_flask.mvc', 'MVC', order=2)
    def mvc(self):
        return render_template('learn_flask/mvc.html')

    @menu.classy_menu_item('frontend.learn_flask.wsgi', 'WSGI vs CGI', order=3)
    def wsgi(self):
        return render_template('learn_flask/wsgi-vs-cgi.html')

    @menu.classy_menu_item('frontend.learn_flask.flask_basics', 'Flask Basics', order=4)
    def flask_basics(self):
        return render_template('learn_flask/flask-basics.html')

    @menu.classy_menu_item('frontend.learn_flask.virtual_env', 'Virtual Environments', order=5)
    def virtualenv(self):
        return render_template('learn_flask/virtualenv.html')

    @menu.classy_menu_item('frontend.learn_flask.using_the_boilerplate', 'Using the Boilerplate', order=7)
    def using_the_boilerplate(self):
        return render_template('learn_flask/using-the-boilerplate.html')


    @menu.classy_menu_item('frontend.learn_flask.starting_up', 'Starting Up', order=6)
    def starting_up(self):
        return render_template('learn_flask/starting-up.html')

    @menu.classy_menu_item('frontend.learn_flask.deploying', 'Deploying', order=9)
    def deploying(self):
        return render_template('learn_flask/deploying.html')

