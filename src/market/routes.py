from flask import Blueprint, current_app, jsonify, request

from src.database.operations import select

market_bp = Blueprint("market", __name__)


@market_bp.route("/")
def market_index():
    return "Hello from market"


@market_bp.route("/items")
def get_item_handler():
    sql = "select * from items"
    if item_id := request.args.get("id"):
        sql = f"select * from items where item_id={item_id}"
        result = select(db_config=current_app.config["DB_CONFIG"], sql=sql)
        if result:
            return jsonify({"status": 200, "item": result[0]})
        return jsonify({"status": 404, "message": "Not found"})
    result = select(db_config=current_app.config["DB_CONFIG"], sql=sql)
    return jsonify({"status": 200, "items": result})


def my_sum(a, b):
    return a + b
