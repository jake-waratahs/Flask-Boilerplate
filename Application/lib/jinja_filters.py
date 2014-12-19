from flask.ext.babel import format_datetime, format_date
from flask import render_template
from datetime import datetime
from urllib.parse import quote
from Application import app
import os
import json

def configure_filters(app):
    # app.jinja_env.filters['] = func
    app.jinja_env.globals['html_assets'] = get_autoincluded_assets()
    app.jinja_env.filters['local_date'] = local_date
    app.jinja_env.filters['local_date_time'] = local_date_time
    app.jinja_env.filters['percent_escape'] = percent_escape
    app.jinja_env.filters['time_since'] = timesince

def local_date_time(datestamp):
    if datestamp:
        return format_datetime(datestamp)

def get_autoincluded_assets():
    fn = os.path.realpath(
        os.path.join(
            app.config['APPLICATION_FOLDER_ROOT'], './static/vendor/autoinclude.json'))
    
    data = None
    with open(fn, 'r') as f:
        data = json.loads(f.read())

    if data and 'scripts' in data and 'stylesheets' in data:
        with app.app_context():
            return render_template('utilities/sources.html', 
                scripts=data['scripts'], 
                stylesheets=data['stylesheets'])


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
