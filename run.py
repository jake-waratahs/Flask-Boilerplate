#!./.venv/bin/python3

import os
os.system('./.venv/bin/pip3 -v -V')
import flask
print (flask)

from Application import app
from flask_boilerplate_utils.commands import MainManager
manager = MainManager(app,with_default_commands=False)

if __name__ == "__main__":
    manager.run(default_command="server")