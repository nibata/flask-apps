from ..controllers.default_controller import DefaultController
from flask import Blueprint, current_app

default_bp = Blueprint("default_bp", __name__)

default_controller = DefaultController(current_app=current_app)

default_bp.route("/", methods=["GET"])(default_controller.index)
