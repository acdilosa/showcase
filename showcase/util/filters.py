from .. import app
import datetime

@app.template_filter('date')
def date_to_string(date, format):
    """Convert a Date to String of specified format"""
    return date.strftime(format)