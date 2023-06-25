from art import text2art
from flask import Flask
from .routes.users_bp import users_bp
from .routes.default_bp import default_bp
from .controllers.default_controller import DefaultController


app = Flask(__name__,
            instance_relative_config=True)

# Configuración de la app
app.config.from_pyfile(filename="config.py")
app_name = app.config["APP_NAME"]
app.config['JSON_AS_ASCII'] = False

welcome = text2art(app_name)
print(welcome)

# Register BluePrints
app.register_blueprint(default_bp, url_prefix="/")
app.register_blueprint(users_bp, url_prefix="/users")

# Error pages
app.register_error_handler(404, DefaultController.page_not_found)
app.register_error_handler(500, DefaultController.server_error)

