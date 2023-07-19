from flask import render_template
from ..auth.users import User


class DefaultController:
    def __init__(self, current_app):
        self.current_app = current_app

    def index(self):
        self.current_app.logger.info("HELLO WORLD!!!")
        return render_template('views/default/index.html')

    @staticmethod
    def page_not_found(e):
        return render_template('views/default/404.html'), 404

    @staticmethod
    def server_error(e):
        return render_template("views/default/500.html"), 500
