import requests


def line_status(url):
    '''Method to call the https://api.tfl.gov.uk/Line/Mode/{modes}/Disruption
    endpoint to return the distruption on the given line'''
    response = requests.get(url)
    return response.status_code, response.json()
