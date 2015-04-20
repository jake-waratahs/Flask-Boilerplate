from flask_boilerplate_utils.overrides import NestableBlueprint
from flask.ext import menu

frontend = NestableBlueprint('frontend', __name__, template_folder="templates", 
    static_folder="static")

from .controllers.Index import Index
Index.register(frontend)
menu.register_flaskview(frontend, Index)


from .modules.submodule import submodule
from .modules.learn_flask import learn_flask
frontend.register_blueprint(submodule, url_prefix='/submodule/<int:id>')
frontend.register_blueprint(learn_flask, url_prefix='/learn-flask')



