import os, sys
from .keys import SECRET_KEY, SECURITY_PASSWORD_SALT

print (SECRET_KEY)
print(SECURITY_PASSWORD_SALT)

class Config(object):	
	APP_NAME = 'Boilerplate'
	_CONFIG_DB_BASE = 'boilerplate'
	SECURITY_PASSWORD_SALT = 'change me'
	SECRET_KEY = 'change me'


	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 587
	MAIL_USE_SSL = False
	MAIL_USERNAME = ''
	MAIL_PASSWORD = ''

	BABEL_DEFAULT_LOCALE = 'en'
	BABEL_DEFAULT_TIMEZONE = 'Australia/Sydney'

	# Security Configuration
	SECURITY_RECOVERABLE = True
	SECURITY_CHANGEABLE = True
	SECURITY_EMAIL_SENDER = 'security@localhost'
	SECURITY_UNAUTHORIZED_VIEW = '/unauthorised'
	
	SECURITY_PASSWORD_HASH = 'bcrypt'

	
class Production(Config):
	DB_DRIVER = 'mysql+pymysql'
	SQLALCHEMY_DATABASE_URI = '%s://%s:%s@127.0.0.1/%s' % (
		DB_DRIVER, 
		'username',
		'password',
		Config._CONFIG_DB_BASE,
		)

	SQLALCHEMY_POOL_SIZE = 20
	SQLALCHEMY_POOL_RECYCLE = 30

	SENTRY_DSN = ''

class Development(Config):
	DEBUG = True
	DB_DRIVER = 'sqlite'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///%s.db' % Config._CONFIG_DB_BASE

class MySQLStd(Development):
	# For use with TwoPi Std SQL Development Setup
	_CONFIG_DB_NAME = 'DEV_%s' % Development._CONFIG_DB_BASE
	_CONFIG_DB_USER = 'dev'
	DB_DRIVER = 'mysql+pymysql'
	SQLALCHEMY_DATABASE_URI = '%s://dev@127.0.0.1/%s' % (DB_DRIVER,_CONFIG_DB_NAME)


class CI(Production):
	SQLALCHEMY_ECHO = False
	_CONFIG_DB_NAME = 'CI_%s' % Production._CONFIG_DB_BASE
	_CONFIG_DB_USER = 'ci'
	DB_DRIVER = 'mysql+pymysql'
	SQLALCHEMY_DATABASE_URI = '%s://ci@127.0.0.1:3306/%s' % (DB_DRIVER,_CONFIG_DB_NAME)
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

