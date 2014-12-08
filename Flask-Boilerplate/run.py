from Application import app
from flask.ext.script import Manager, Command, Option


class Run(Command):
	"Run the Flask Builtin Server (Not for production)"

	option_list = (
		Option('--hostname', '-h', dest='hostname', default='0.0.0.0', type=str),
		Option('--port', '-p', dest='port', default=8000, type=int),
		Option('--debug', '-d', dest='debug', default=False, action='store_true'),
	)

	def run(self, port, hostname, debug):
		app.run(debug=debug, host=hostname, port=port)


manager = Manager(app,with_default_commands=False)

manager.add_command('server', Run())
if __name__ == "__main__":
    manager.run(default_command="server")