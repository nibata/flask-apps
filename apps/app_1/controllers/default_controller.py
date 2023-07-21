from ..services.translate import format_date, gettext
from flask import render_template
from datetime import date


class DefaultController:
    def __init__(self, current_app):
        self.current_app = current_app

    def index(self):
        self.current_app.logger.info("HELLO WORLD!!!")

        d = date(2022, 11, 24)
        formated_date = format_date(d)

        word = gettext("word")
        hello = gettext("hello")
        world = gettext("world")

        return render_template('views/default/index.html', formated_date=formated_date, word=word, hello=hello,
                               world=world)

    @staticmethod
    def page_not_found(e):
        return render_template('views/default/404.html'), 404

    @staticmethod
    def server_error(e):
        return render_template("views/default/500.html"), 500
