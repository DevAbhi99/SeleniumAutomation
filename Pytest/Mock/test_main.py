from main import getWeather
import pytest


def test_getWeather(mocker):
    mock_get=mocker.patch('main.requests.get')

    mock_get.return_value.status_code=200   #sets my own return value of a json creating fake response
    mock_get.return_value.json.return_value={'temperature':21, 'weather':'sunny'}

    result=getWeather('Dubai') #storing the value obtained from the function

    assert result=={'temperature':21, 'weather':'sunny'} #Testing using mock
    mock_get.assert_called_once_with('https://api.weather.com/v1/Dubai') #using the main api