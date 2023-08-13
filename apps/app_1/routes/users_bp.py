from ..controllers.users_controller import UsersController
from flask import Blueprint

users_bp = Blueprint("users_bp", __name__)

user_controller = UsersController()

users_bp.route("/", methods=["GET"])(user_controller.index)

users_bp.route("/data", methods=["GET"])(user_controller.data)
