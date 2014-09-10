from Application import app
import sys

if '--help' in sys.argv or '-?' in sys.argv:
	print "Usage: ./%s  [(--hostname|-h) <0.0.0.0>] [(-p|--port) <8000>] [--debug|-d]" % (sys.argv[0])
	exit()

debug = 'False'
host = '0.0.0.0'
port = '8000'


if '--hostname' in sys.argv:
	pos = sys.argv.index('--hostname') + 1
	host = sys.argv[pos]

if '-h' in sys.argv:
	pos = sys.argv.index('-h') + 1
	host = sys.argv[pos]

if '--port' in sys.argv:
	pos = sys.argv.index('--port') +1
	port = sys.argv[pos]

if '-p' in sys.argv:
	pos = sys.argv.index('-p') + 1
	port = sys.argv[pos]
	

if '--debug' in sys.argv or '-d' in sys.argv:
	print " * Warning: Running Debug"
	debug = True



app.run(debug=debug, host=host, port=int(port))
