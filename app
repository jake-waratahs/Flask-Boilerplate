#!/usr/bin/env python3
from config import get_config
from flask_boilerplate_buildutils.run import run_app
# Build project dependencies before importing the app.
config = get_config()
config.build_dependencies()

# Run the app
run_app()