from flask.ext.babel import format_datetime, format_date
from datetime import datetime
from urllib import quote


def configure_filters(app):
	# app.jinja_env.filters['] = func
	# app.jinja_env.globals['test'] = 'Hello World'
	app.jinja_env.filters['local_date'] = local_date
	app.jinja_env.filters['local_date_time'] = local_date_time
	app.jinja_env.filters['percent_escape'] = percent_escape
	app.jinja_env.filters['time_since'] = timesince

def local_date_time(datestamp):
    if datestamp:
        return format_datetime(datestamp)

def local_date(datestamp):
    return format_date(datestamp)

def percent_escape(string):
    return quote(string, '')

def timesince(dt, default="Just now."):
    """
    Returns string representing "time since" e.g.
    3 days ago, 5 hours ago etc.
    """

    now = datetime.now()
    diff = now - dt
    
    periods = (
        (diff.days / 365, "year", "years"),
        (diff.days / 30, "month", "months"),
        (diff.days / 7, "week", "weeks"),
        (diff.days, "day", "days"),
        (diff.seconds / 3600, "hour", "hours"),
        (diff.seconds / 60, "minute", "minutes"),
        (diff.seconds, "second", "seconds"),
    )

    for period, singular, plural in periods:
        
        if period:
            return "%d %s ago" % (period, singular if period == 1 else plural)

    return default
