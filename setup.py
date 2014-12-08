from distutils.core import setup
setup(
  name = 'Flask-Boilerplate',
  package_data={'Flask-Boilerplate':'Flask-Boilerplate'},
  version = '0.9.0',
  description = 'A Boilerplate for flask with a bunch of utilities',
  author = 'Nick Whyte',
  author_email = 'nick@nickwhyte.com',
  url = 'https://github.com/nickw444/flask-boilerplate', # use the URL to the github repo
  download_url = 'https://github.com/nickw444/flask-boilerplate/tarball/0.9.0',
  keywords = ['flask', 'boilerplate', 'utility'], 
  classifiers = [],
  scripts=['scripts/foiler'],
  install_requires=[
        "flask",
        "virtualenv",
        "flask-script",
    ],
)