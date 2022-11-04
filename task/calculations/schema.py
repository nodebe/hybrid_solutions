from pydantic import BaseModel


class CalculationBody(BaseModel):
    operation_type: str
    x: int
    y: int

class SuccessResponseSchema(BaseModel):
    slackUsername: str
    operation_type: str
    result: int | float

class NoOperationResponseSchema(BaseModel):
    message: str