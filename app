#!.venv/bin/python

from Application import app
from flask.ext.script import Manager, Command, Option


class Run(Command):
	"Run the Flask Builtin Server (Not for production)"

	option_list = (
		Option('--hostname', '-h', dest='hostname', default='0.0.0.0', type=str),
		Option('--port', '-p', dest='port', default=8000, type=int),
		Option('--debug', '-d', dest='debug', default=True, action='store_true'),
	)

	def run(self, port, hostname, debug):
		app.run(debug=debug, host=hostname, port=port)

class Host(Command):
	"""
	Run a Web Server for Hosting using meinheld.
	"""

	option_list = (
		Option('--hostname', '-h', dest='hostname', default='0.0.0.0', type=str),
		Option('--port', '-p', dest='port', default=8000, type=int),
	)
	def run(self, port, hostname):
		from meinheld import server, patch
		patch.patch_all()
		print(" - Running Hosting Server using Meinheld")
		print(" - http://%s:%s/" % (hostname, port))
		server.listen((hostname, port))
		server.run(app)

from commands.InstallFramework import InstallFramework


manager = Manager(app,with_default_commands=False)
manager.add_command('server', Run())
manager.add_command('meinheld', Host())
manager.add_command('install', InstallFramework())


if __name__ == "__main__":
    manager.run(default_command="server")