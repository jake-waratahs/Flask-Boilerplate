from distutils.core import setup
import os 

p = os.path.join(os.path.dirname(os.path.realpath(__file__)), './flask_boilerplate/boilerplate/')
replace = os.path.join(os.path.dirname(os.path.realpath(__file__)), './flask_boilerplate/')
p = os.path.realpath(p)
replace = os.path.realpath(replace) + '/'


data = []

for dirname, dirnames, filenames in os.walk(p):
    for filename in filenames:
        f = os.path.join(dirname, filename)
        if not f.endswith('.pyc'):
          data.append(f.replace(replace, ''))


setup(
  name = 'Flask-Boilerplate',
  packages = ['flask_boilerplate'],
  package_data={'flask_boilerplate':
    data},
  version = '1.0.1',
  description = 'A Boilerplate for flask with a bunch of utilities',
  author = 'Nick Whyte',
  author_email = 'nick@nickwhyte.com',
  url = 'https://github.com/nickw444/flask-boilerplate', # use the URL to the github repo
  download_url = 'https://github.com/nickw444/flask-boilerplate/tarball/1.0.1',
  keywords = ['flask', 'boilerplate', 'utility'], 
  classifiers = [],
  scripts=['scripts/foiler'],
  install_requires=[
        "Flask",
        "virtualenv",
        "flask-script",
    ],
)