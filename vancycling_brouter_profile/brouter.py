from typing import List, Tuple
from requests import Session, Request
from config import log

BROUTER_BASE_URL = "https://www.brouter.de/"
WEB_PREFIX = "brouter-web/#map=13/49.2743/-123.1351/standard"
PROFILE_ID = "custom_1694894568334"


def set_profile(profile):
    session = Session()
    resource_url = BROUTER_BASE_URL + "brouter/profile/" + PROFILE_ID
    request = Request("POST", resource_url, data=profile).prepare()
    response = session.send(request)
    log.debug(response.json())
    return response


def get_route_geojson(points: List[Tuple[int, int]]):
    session = Session()
    resource_url = BROUTER_BASE_URL + "brouter"
    params = {
        "lonlats": "|".join([f"{p.lon},{p.lat}" for p in points]),
        "profile": PROFILE_ID,
        "alternativeidx": 0,
        "format": "geojson",
    }
    log.debug(
        f"{BROUTER_BASE_URL}{WEB_PREFIX}&lonlats=%s",
        ";".join([f"{p.lon},{p.lat}" for p in points]),
    )
    request = Request("GET", resource_url, params=params).prepare()
    response = session.send(request)
    route_props = response.json()["features"][0]["properties"]
    log.debug({k: v for k, v in route_props.items() if k not in ["messages", "times"]})
    return response.json()
