from flask_boilerplate_utils.overrides import NestableBlueprint

examples = NestableBlueprint('frontend.examples', __name__, template_folder="templates", 
    static_folder="static")

from .controllers.MainController import MainController
from .controllers.UploadsController import UploadsController
from .controllers.SecurityController import SecurityController
from .controllers.WTFormsController import WTFormsController
from .controllers.Features import Features
Features.register(examples)
MainController.register(examples)
UploadsController.register(examples)
SecurityController.register(examples)
WTFormsController.register(examples)

from flask.ext import menu
menu.register_flaskview(examples, MainController)
menu.register_flaskview(examples, UploadsController)
menu.register_flaskview(examples, SecurityController)
menu.register_flaskview(examples, WTFormsController)
menu.register_flaskview(examples, Features)

from .modules.submodule import submodule
examples.register_blueprint(submodule, url_prefix='/submodule/<int:id>')