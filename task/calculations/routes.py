from flask import Blueprint
from flask_pydantic import validate
from .calculation_utils import add, subtract, multiply, divide
from .schema import CalculationBody, SuccessResponseSchema, NoOperationResponseSchema

calculation_route = Blueprint('calculation', __name__)

@calculation_route.post('/calculator')
@validate()
def calculator(body: CalculationBody):
    operation_type = body.operation_type
    x = body.x
    y = body.y

    operations = {
        'addition': add,
        'subtraction': subtract,
        'multiplication': multiply,
        'division': divide
    }
    # Synonyms of operations that will be searched in operation_type string
    operations_synonyms = {
        'add': add,
        'plus': add,
        'minus': subtract,
    }
    operations.update(operations_synonyms)

    operation_type_sentence = operation_type.split(' ')
    
    # Checking if any word in sentence matches any of the operations in the given dictionary
    for word in operation_type_sentence:
        if word in operations:
            result = operations[word](x, y)

            return SuccessResponseSchema(
            slackUsername = 'KayKay',
            operation_type = word,
            result = result
        ), 200
    
    return NoOperationResponseSchema(
            slackUsername = 'KayKay',
            operation_type = operation_type,
            result = 0
        ), 400