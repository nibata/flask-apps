from ..controllers.stock_movement_controller import StockMoveController
from flask import Blueprint, current_app

stock_bp = Blueprint("stock_move_bp", __name__)

stock_controller = StockMoveController()

stock_bp.route("/", methods=["GET"])(stock_controller.index)

stock_bp.route("/data", methods=["GET"])(stock_controller.data)