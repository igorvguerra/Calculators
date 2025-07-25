from flask import Blueprint, jsonify, request
from src.main.factories.calculator_1_factory import calculator1_factory
from src.main.factories.calculator_2_factory import calculator2_factory
from src.main.factories.calculator_3_factory import calculator3_factory

from src.errors.error_controller import handle_errors


calc_rout_bp = Blueprint("calc_routes", __name__)

@calc_rout_bp.route("/calculator/1", methods=['POST'])
def calculator_1():
    try:
        calc = calculator1_factory()
        response = calc.calculate(request)
        return jsonify(response)
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]


@calc_rout_bp.route("/calculator/2", methods=['POST'])
def calculator_2():
    try:
        calc = calculator2_factory()
        response = calc.calculate(request)
        return jsonify(response)
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]


@calc_rout_bp.route("/calculator/3", methods=['POST'])
def calculator_3():
    try:
        calc = calculator3_factory()
        response = calc.calculate(request)
        return jsonify(response)
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]