from main import isEven
import pytest


@pytest.mark.parametrize("num, expected", [
    (1,False),
    (2, True),
    (3, False),
    (4, True),
    (5,True)
])

def test_isEven(num, expected):
    assert isEven(num)==expected