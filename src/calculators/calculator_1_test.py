from .calculator_1 import Calculator1
from pytest import raises
from typing import Dict

class MockRequest:
    def __init__(self, body: Dict):
        self.json = body

def test_calculate():
    mock_request = MockRequest(body={"number": 1})
    calculator_1 = Calculator1()

    response = calculator_1.calculate(mock_request)
   
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "Result" in response["data"]

    assert response["data"]["Result" ] == 14.25
    assert response["data"]["Calculator"] == 1

def test_calculate_with_body_error():
    mock_request = MockRequest(body={"something": 1})
    calculator_1 = Calculator1()

    with raises(Exception) as excinfo:
       calculator_1.calculate(mock_request)
    assert str(excinfo.value) == "wrong format for Body!"