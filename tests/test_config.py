from src import config
from unittest import mock


@mock.patch('src.config.tfl_api_keys', return_value={'app_id': 'ABC123',
                                                     'app_key': '123ABC'})
def test_tfl_api_key(mocked_api_key):
    '''Test method to verify the tfl_api_keys method from config.py retruns the
        TFL API keys in the correct format'''
    assert config.tfl_api_keys() == {'app_id': 'ABC123', 'app_key': '123ABC'}
