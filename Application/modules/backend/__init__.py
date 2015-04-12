from flask_boilerplate_utils.overrides import NestableBlueprint

backend = NestableBlueprint('backend', __name__, template_folder="templates", 
    static_folder="static")

from .controllers.Index import Index
Index.register(backend)
