from art import text2art
from flask import Flask

from datetime import timedelta

from .routes.default_bp import default_bp
from .routes.table_bp import tables_bp
from .routes.login_bp import login_bp
from .routes.users_bp import users_bp
from .routes.graph_bp import graph_bp
from .routes.stock_bp import stock_bp

from .controllers.default_controller import DefaultController

from .services.login_manager import login_manager
from .services.translate import babel, get_locale
from .services.csrf_protection import csrf


app = Flask(__name__,
            instance_relative_config=True)

# Configuración de la app
app.config.from_pyfile(filename="config.py")
app_name = app.config["APP_NAME"]
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)

# Register BluePrints
app.register_blueprint(default_bp, url_prefix="/")
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(login_bp, url_prefix="/auth")
app.register_blueprint(graph_bp, url_prefix="/graph")
app.register_blueprint(tables_bp, url_prefix="/tables")
app.register_blueprint(stock_bp, url_prefix="/stock")

# Error pages
app.register_error_handler(404, DefaultController.page_not_found)
app.register_error_handler(500, DefaultController.server_error)

# Inicialización de servicios
login_manager.init_app(app=app)
login_manager.login_view = "/auth/login"


# CSRF protection
csrf.init_app(app=app)

babel.init_app(app=app, locale_selector=get_locale)

# Print de inicio
print(text2art("Welcome to"))
print(text2art(app_name))
