from flask_boilerplate_utils.overrides import NestableBlueprint

learn_flask = NestableBlueprint('learn_flask', __name__, template_folder="templates", 
    static_folder="static")

from .controllers.Index import Index
Index.register(learn_flask)

from flask.ext import menu
menu.register_flaskview(learn_flask, Index)