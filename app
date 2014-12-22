#!/usr/bin/env python3
from config import get_config
import sys, os
# Build project dependencies before importing the app.
config = get_config()
config.build_dependencies()

os.system('source ./.venv/bin/activate && unset __PYVENV_LAUNCHER__ && python3 ./run.py {args}'.format(
	args=' '.join(list(map(lambda x: "'{arg}'".format(arg=x), sys.argv[1:])))
	))
