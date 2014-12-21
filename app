#!/usr/bin/env python3
from config import get_config
import sys, os
import subprocess
# Build project dependencies before importing the app.
config = get_config()
config.build_dependencies()

# Run the app
# os.system('./.venv/bin/python3 ./run.py %s' % ' '.join(sys.argv[1:]))
subprocess.Popen('./run.py %s' % ' '.join(sys.argv[1:]), 
	shell=True)