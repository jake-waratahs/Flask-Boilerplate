#!./.venv/bin/python3
import Application
import unittest

class FlaskTestClientProxy(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        environ['REMOTE_ADDR'] = environ.get('REMOTE_ADDR', '127.0.0.1')
        environ['HTTP_USER_AGENT'] = environ.get('HTTP_USER_AGENT', 'Chrome')
        return self.app(environ, start_response)

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        Application.app.wsgi_app = FlaskTestClientProxy(Application.app.wsgi_app)
        Application.app.config['TESTING'] = True
        Application.app.config['WTF_CSRF_ENABLED'] = False
        self.app = Application.app.test_client()
        self._app = Application.app

    def tearDown(self):
        pass

    def test_sample(self):
        response = self.app.get('/')
        assert '' in response.data.decode('UTF-8')

if __name__ == '__main__':
    unittest.main()
