#!/usr/bin/env python3
from flask_boilerplate_buildutils.run import run_app, patch_cwd
# Patch the current working directory so that 
# you can run this script without being cd'd
# into the directory it resides.
patch_cwd()

from config import get_config
# Build project dependencies before importing the app.
config = get_config()
config.build_dependencies()

# Run the app

run_app()