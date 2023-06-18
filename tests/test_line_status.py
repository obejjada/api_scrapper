import pytest
from src import line_status

good_url_tube = 'https://api.tfl.gov.uk/Line/Mode/tube/Disruption'
bad_url_tube = 'https://api.tfl.gov.uk/Line/Mode/flyingsaucer/Disruption'
incorect_url_tube = 'https://api.tfl.gov.NZ/Line/Mode/tube/Disruption'


def test_line_status_http_good_response():
    '''Method to verify a line status method returns HTTP response of 200 when
    the URL is correct'''
    assert line_status.line_status(good_url_tube)[0] == 200


def test_line_status_http_bad_response():
    '''Method to verify a line status method returns HTTP response of 400 when
    the URL contains an incorrect parameter'''
    assert line_status.line_status(bad_url_tube)[0] == 400


def test_line_status_incorect_url():
    '''Method to verify a line status method raises a TypeError expection when
    an incorrect URL is used'''
    with pytest.raises(Exception) as exc_info:
        line_status.line_status(incorect_url_tube)
        assert exc_info == TypeError
