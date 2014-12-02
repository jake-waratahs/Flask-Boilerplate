import os, sys
import variables as variables

class Config(object):
	if not variables.SECRET_KEY:
		raise Exception("No Secret Key Defined in variables.py!")
	SECRET_KEY = variables.SECRET_KEY

	if not variables.SECURITY_PASSWORD_SALT:
		raise Exception("No Password salt Defined in variables.py!")


	MAIL_SERVER = variables.MAIL_SERVER
	MAIL_PORT = variables.MAIL_PORT
	MAIL_USE_SSL = variables.MAIL_USE_SSL
	MAIL_USERNAME = variables.MAIL_USERNAME
	MAIL_PASSWORD = variables.MAIL_PASSWORD

	BABEL_DEFAULT_LOCALE = variables.BABEL_DEFAULT_LOCALE
	BABEL_DEFAULT_TIMEZONE = variables.BABEL_DEFAULT_LOCALE

	# Security Configuration
	SECURITY_RECOVERABLE = True
	SECURITY_CHANGEABLE = True
	SECURITY_EMAIL_SENDER = 'security@localhost'
	SECURITY_UNAUTHORIZED_VIEW = '/unauthorised'
	SECURITY_PASSWORD_SALT = variables.SECURITY_PASSWORD_SALT
	SECURITY_PASSWORD_HASH = 'bcrypt'

	_CONFIG_DB_BASE = variables.DB_BASE

class Production(Config):
	SQLALCHEMY_DATABASE_URI = '%s://%s:%s@127.0.0.1/%s' % (
		variables.PRODUCTION_DB_DRIVER, 
		variables.PRODUCTION_DB_USER,
		variables.PRODUCTION_DB_PASSWORD,
		variables.PRODUCTION_DB_DATABASE,
		)

	SQLALCHEMY_POOL_SIZE = 20
	SQLALCHEMY_POOL_RECYCLE = 30

	if variables.SENTRY_DSN:
		SENTRY_DSN = variables.SENTRY_DSN


class Development(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///%s.db' % variables.DB_BASE

class MySQLStd(Development):
	# For use with TwoPi Std SQL Development Setup
	_CONFIG_DB_NAME = 'DEV_%s' % variables.DB_BASE
	_CONFIG_DB_USER = 'dev'
	SQLALCHEMY_DATABASE_URI = 'mysql://dev@127.0.0.1/%s' % _CONFIG_DB_NAME


class CI(Production):
	SQLALCHEMY_ECHO = False
	_CONFIG_DB_NAME = 'CI_%s' % variables.DB_BASE
	_CONFIG_DB_USER = 'ci'
	SQLALCHEMY_DATABASE_URI = 'mysql://ci@127.0.0.1:3306/%s' % _CONFIG_DB_NAME
	DEBUG = True


def get_config():
	if os.environ.get('BUILD_ID') or os.environ.get('CI_BUILD_ID'):
		return CI
	elif '-prod' in sys.argv or os.environ.get('PRODUCTION'):
		return Production
	elif os.environ.get('MYSQL_DEV'):
		return MySQLStd
	else:
		return Development

