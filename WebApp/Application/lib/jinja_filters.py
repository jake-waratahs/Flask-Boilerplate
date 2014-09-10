
def insert_filters(app):
	# app.jinja_env.filters['] = func
	app.jinja_env.globals['test'] = 'Hello World'


