from ..controllers.login_controller import login, logout
from flask import Blueprint

login_bp = Blueprint("login_bp", __name__)

login_bp.route("/login", methods=["GET", "POST"])(login)

login_bp.route("/logout", methods=["GET", "POST"])(logout)
