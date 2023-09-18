from requests import Session, Request
from config import log

BROUTER_BASE_URL = "https://www.brouter.de/"
PROFILE_ID = "custom_1694894568334"


def set_profile(profile):
    session = Session()
    resource_url = BROUTER_BASE_URL + "brouter/profile"
    request = Request("POST", resource_url).prepare()
    response = session.send(request)
    return response


def get_route(points):
    session = Session()
    resource_url = BROUTER_BASE_URL + "brouter"
    params = {
        "lonlats": "",
        "profile": PROFILE_ID,
        "alternativeidx": 0,
        "format": "geojson",
    }
    request = Request("POST", resource_url, params=params).prepare()
    response = session.send(request)
    return response
