import sys

from flask_boilerplate_utils.configuration import (
	SECRET_KEY, 
	SECURITY_PASSWORD_SALT,
)

class Config(object):	
	# General App Config
	APP_NAME = 'Boilerplate'
	DB_BASE = 'boilerplate'
	
	# Mail Configuration
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 587
	MAIL_USE_SSL = False
	MAIL_USERNAME = ''
	MAIL_PASSWORD = ''

	# Babel configuration
	BABEL_DEFAULT_LOCALE = 'en'
	BABEL_DEFAULT_TIMEZONE = 'Australia/Sydney'

	# Security Configuration
	SECURITY_RECOVERABLE = True
	SECURITY_CHANGEABLE = True
	SECURITY_EMAIL_SENDER = 'security@localhost'
	SECURITY_UNAUTHORIZED_VIEW = '/unauthorised'	
	SECURITY_PASSWORD_HASH = 'bcrypt'
	SECURITY_PASSWORD_SALT = SECURITY_PASSWORD_SALT
	SECRET_KEY = SECRET_KEY


	
class Production(Config):
	# SQL Configuration for Production
	DB_DRIVER = 'mysql+pymysql'
	DB_USERNAME = 'username'
	DB_PASSWORD = 'password'
	DB_HOST = '127.0.0.1'
	DB_DATABASE = ''

	SENTRY_DSN = ''

	SQLALCHEMY_DATABASE_URI = '%s://%s:%s@%s/%s' % (
			DB_DRIVER, 
			DB_USERNAME,
			DB_PASSWORD,
			DB_HOST,
			DB_DATABASE,
		)

class Development(Config):

	DEBUG = True
	DB_DRIVER = 'sqlite'


	SQLALCHEMY_DATABASE_URI = '%s:///%s.db' % (
		DB_DRIVER,
		Config.DB_BASE
	)

class MySQLStd(Development):
	# For use with TwoPi Std SQL Development Setup
	# See readme

	DB_DRIVER = 'mysql+pymysql'
	DB_USERNAME = 'dev'
	DB_HOST = '127.0.0.1'
	DB_DATABASE = 'DEV_%s' % Development.DB_BASE

	SQLALCHEMY_DATABASE_URI = '%s://%s@%s/%s' % (
			DB_DRIVER, 
			DB_USERNAME,
			DB_HOST,
			DB_DATABASE,
		)

class CI(Production):
	SQLALCHEMY_ECHO = False
	DEBUG = True

	DB_DRIVER = 'mysql+pymysql'
	DB_USERNAME = 'ci'
	DB_HOST = '127.0.0.1'
	DB_DATABASE = 'CI_%s' % Development.DB_BASE

	SQLALCHEMY_DATABASE_URI = '%s://%s@%s/%s' % (
			DB_DRIVER, 
			DB_USERNAME,
			DB_HOST,
			DB_DATABASE,
		)
	

def get_config():
	"""
	Choose a configuration class.
	Flask Boilerplate Utils will choose one depending on 
	your Environment Variables. 

	Set FLASK_CONFIG=<CLASS NAME> in your bash/zsh profile
	
	export 'FLASK_CONFIG=<CLASS NAME>' >> ~/.bashrc
	export 'FLASK_CONFIG=<CLASS NAME>' >> ~/.zshrc

	Alternatively, invoke the application using the 
	--config or -c argument and supply a class.

	You can also override this function.
	"""
	from flask_boilerplate_utils.configuration import choose_config
	return choose_config(config_module=sys.modules[__name__])

