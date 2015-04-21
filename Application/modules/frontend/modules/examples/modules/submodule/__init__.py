from flask_boilerplate_utils.overrides import NestableBlueprint
from flask.ext import menu

submodule = NestableBlueprint('frontend.examples.submodule', __name__, template_folder="templates", 
    static_folder="static")
submodule.expected_parameters = ['id']

from .controllers.Index import Index
Index.register(submodule)
menu.register_flaskview(submodule, Index)


@submodule.url_value_preprocessor
def validate_id(route, args):
    """
    Here we can validate the passed arguments
    """
    pass

