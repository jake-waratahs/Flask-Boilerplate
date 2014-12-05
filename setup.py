from distutils.core import setup
setup(
  name = 'Flask-Boilerplate',
  packages = [], # this must be the same as the name above
  version = '0.1',
  description = 'A Boilerplate for flask with a bunch of utilities',
  author = 'Nick Whyte',
  author_email = 'nick@nickwhyte.com',
  url = 'https://github.com/nickw444/flask-boilerplate', # use the URL to the github repo
  download_url = 'https://github.com/nickw444/flask-boilerplate/tarball/0.1',
  keywords = ['flask', 'boilerplate', 'utility'], 
  classifiers = [],
  scripts=['scripts/foiler'],
  install_requires=[
        "flask",
        "virtualenv",
    ],
)