#!/usr/bin/env python3
from flask_boilerplate_buildutils.run import run_app, patch_cwd
patch_cwd()

from config import get_config

# Build project dependencies before importing the app.
config = get_config()
config.build_dependencies()

# Run the app
run_app()