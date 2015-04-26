"""
A Module to clean up the boilerplate and delete everything. 
"""

from flask import Blueprint


cleanup = Blueprint('frontend.cleanup', __name__, template_folder="templates", 
    static_folder="static")

from flask.ext.classy import FlaskView, route
from flask.ext import menu
from flask import render_template, request, redirect


class Cleanup(FlaskView):
    route_base = '/'

    @route('/', methods=['GET','POST'])
    @menu.classy_menu_item('frontend.cleanup', 'Cleanup', order=4)
    def index(self):
        if request.method == 'POST':
            import shutil
            print(" * Cleaning up...")
            print(" * Unlinking Submodules")
            kept_lines = None
            with open('./Application/modules/frontend/__init__.py', 'r') as fh:
                kept_lines = fh.readlines()

            with open('./Application/modules/frontend/__init__.py', 'w') as fh:
                for line in kept_lines:
                    if "Pragma - Submodule Registration Start" in line:
                        break

                    fh.write(line)

            print(" * Deleting Submodules")
            shutil.rmtree('./Application/modules/frontend/modules')

            print(" * Deleting Models")
            shutil.rmtree('./libs/models/models/examples')

            print(" * Cleanup Complete!")

            # return redirect('/')

        return render_template('frontend.cleanup/index.html')

Cleanup.register(cleanup)
menu.register_flaskview(cleanup, Cleanup)
