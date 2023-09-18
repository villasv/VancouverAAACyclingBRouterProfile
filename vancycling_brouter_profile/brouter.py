from requests import Session, Request

BROUTER_BASE_URL = "https://www.brouter.de/"
"?lonlats=-123.126527,49.289796|-123.095911,49.28404&profile=custom_1694894568334&alternativeidx=0&format=geojson"

PROFILE_ID = "custom_1694894568334"


def set_profile(profile):
    session = Session()
    resource_url = BROUTER_BASE_URL + "brouter/profile"
    request = Request("POST", resource_url).prepare()
    response = session.send(request)


def get_route(points):
    pass
