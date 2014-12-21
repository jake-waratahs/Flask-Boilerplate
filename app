#!/usr/bin/env python3
from config import get_config
import sys, os
import subprocess
# Build project dependencies before importing the app.
config = get_config()
config.build_dependencies()

with open('._hack.sh', 'w') as f:
	f.write('. ./.venv/bin/activate\n')
	f.write('which python\n')
	f.write('python3 ./run.py %s' % ' '.join(sys.argv[1:]))
	f.write('\ndeactivate')

os.system('/bin/bash ./._hack.sh')

# Run the app
# os.system('./.venv/bin/python3 ./run.py %s' % ' '.join(sys.argv[1:]))
# subprocess.Popen('./run.py %s' % ' '.join(sys.argv[1:]), 
	# shell=True)