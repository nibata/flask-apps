from flask import Blueprint, current_app
from ..controllers.graph_controller import GraphController

graph_bp = Blueprint("graph_bp", __name__)
graph_controller = GraphController(current_app=current_app)

graph_bp.route("/", methods=["GET"])(graph_controller.index)

graph_bp.route("/callback_graph_data", methods=["GET", "POST"])(graph_controller.callback_graph)