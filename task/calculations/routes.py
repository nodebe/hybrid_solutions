from flask import Blueprint
from flask_pydantic import validate
from .calculation_utils import add, subtract, multiply, divide
from .schema import CalculationBody, SuccessResponseSchema, NoOperationResponseSchema

calculation_route = Blueprint('calculation', __name__)

@calculation_route.post('/')
@validate()
def calculate(body: CalculationBody):
    operation_type = body.operation_type
    x = body.x
    y = body.y

    operations = {
        'addition': add,
        'subtraction': subtract,
        'multiplication': multiply,
        'division': divide
    }

    if operation_type in operations:
        result = operations[operation_type](x, y)

    else:
        return NoOperationResponseSchema(
            message = 'Operation does not exist!'
        ), 400

    return SuccessResponseSchema(
        slackUsername = 'KayKay',
        operation_type = operation_type,
        result = result
    ), 200