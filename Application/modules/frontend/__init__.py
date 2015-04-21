from flask_boilerplate_utils.overrides import NestableBlueprint
from flask.ext import menu

frontend = NestableBlueprint('frontend', __name__, template_folder="templates", 
    static_folder="static")

from .controllers.Index import Index
Index.register(frontend)
menu.register_flaskview(frontend, Index)


from .modules.learn_flask import learn_flask
from .modules.examples import examples
frontend.register_blueprint(learn_flask, url_prefix='/learn-flask')
frontend.register_blueprint(examples, url_prefix='/examples')



