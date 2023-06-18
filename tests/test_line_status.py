from unittest import mock
from src import line_status

good_url_tube = 'https://api.tfl.gov.uk/Line/Mode/tube/Disruption'
bad_url_tube = 'https://api.tfl.gov.uk/Line/Mode/flyingsaucer/Disruption'


def test_line_status_http_good_response():
    '''Method to verify a line status HTTP response is returned 200 when the
        URL is correct'''
    assert line_status.line_status(good_url_tube)[0] == 200


def test_line_status_http_bad_response():
    '''Method to verify a line status HTTP response is returned 400 when the
        URL is incorrect'''
    assert line_status.line_status(bad_url_tube)[0] == 400
