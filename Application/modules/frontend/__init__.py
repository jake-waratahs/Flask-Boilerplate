from flask_boilerplate_utils.overrides import NestableBlueprint
from flask.ext import menu

frontend = NestableBlueprint('frontend', __name__, template_folder="templates", 
    static_folder="static")

from .controllers.Index import Index
Index.register(frontend)
menu.register_flaskview(frontend, Index)
