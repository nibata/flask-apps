from flask import Blueprint, current_app
from ..controllers.table_controller import TableController

tables_bp = Blueprint("tables_bp", __name__)

table_controller = TableController(current_app=current_app)

tables_bp.route("/", methods=["GET"])(table_controller.index)

tables_bp.route("/manual_conf", methods=["GET"])(table_controller.manual_conf)

tables_bp.route("/data", methods=["GET"])(table_controller.data)
