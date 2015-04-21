from flask_boilerplate_utils.overrides import NestableBlueprint

learn_flask = NestableBlueprint('frontend.learn_flask', __name__, template_folder="templates", 
    static_folder="static")

from .controllers.MainController import MainController
MainController.register(learn_flask)

from flask.ext import menu
menu.register_flaskview(learn_flask, MainController)

import os
examples_dir = os.path.realpath(os.path.join(os.path.realpath(__file__), '../python_examples/'))
@learn_flask.app_template_global('load_example_with_name')
def load_example_with_name(filename):
    fpath = os.path.join(examples_dir, filename)
    with open(fpath) as fh: 
        return fh.read()
