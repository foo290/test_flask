import requests

API = "https://ipgeolocation.abstractapi.com/v1/"
API_KEY = 'b04a3d689f66455eabe7a9e248f67948'

VALID_CODES = [200]


def locate_ip(ip: str):
    params = {
        'api_key': API_KEY,
        'ip_address': ip,
    }
    resp = requests.get(API, params=params)
    if resp.status_code in VALID_CODES:
        return resp.json()
    return resp.content
