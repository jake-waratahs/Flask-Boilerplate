from flask_boilerplate_utils.overrides import NestableBlueprint

examples = NestableBlueprint('frontend.examples', __name__, template_folder="templates", 
    static_folder="static")

from .controllers.MainController import MainController
MainController.register(examples)

from flask.ext import menu
menu.register_flaskview(examples, MainController)

from .modules.submodule import submodule
examples.register_blueprint(submodule, url_prefix='/submodule/<int:id>')