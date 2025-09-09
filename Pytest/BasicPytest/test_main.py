from main import getWeather, add, divide
import pytest

def testGetWeather():
    assert getWeather(21)=='HOT'


def testadd():
    assert add(1,2)==3


def testdivide():
    with pytest.raises(ValueError, match="cannot divide by zero"):
        divide(1.0)