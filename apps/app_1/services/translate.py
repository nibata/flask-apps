from flask_babel import Babel, format_date, gettext
from flask import request

babel = Babel()


def get_locale():
    return request.accept_languages.best_match(['de', 'es', 'en'])
