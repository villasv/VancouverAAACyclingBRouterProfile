from typing import List, Optional
from collections import namedtuple
from pathlib import Path

import brouter
from config import log

LonLat = namedtuple("LonLat", "lon lat")


class Router:
    def __init__(self):
        self.profile = self.compile()
        brouter.set_profile(self.profile)

    def assign_pedestrian_penalty(self, **context):
        """
        Avoid pedestrian infrastructure, but not too much! The bicycle is the
        only vehicle that can be carried around by foot in pedestrian paths,
        it's a very useful feature.

        Lost Lagoon to Rawlings Trail: should take the small pedestrian bridge.
        This pedestrian-only section is very small and has low foot traffic, and
        it connects two adjacent bike paths. The alternative would be taking the
        Stanley Park Seawall Bike Path around Ceperley Meadow, but the
        difference in distance is not worth it.

        >>> route = router.eval([LonLat(-123.145752, 49.295477), LonLat(-123.150858,49.296597)])
        >>> len([p for p in route if 'footway' in p['WayTags']])
        2

        Third Beach to Second Beach (should prefer Seawall)

        Seaside Path vs Beach Avenue Lane
        https://brouter.de/brouter-web/#map=15/49.2898/-123.1474/standard&lonlats=-123.150913,49.296269;-123.135583,49.277691

        Convention Center stairs vs Seawall lane
        """
        return

    def compile(self):
        """
        Not implemented yet, just return the manually crafted one.
        """
        DEFAULT_PROFILE_PATH = "vancycling.brf"
        return Path(DEFAULT_PROFILE_PATH).read_text()

    def eval(self, points: List[LonLat]):
        geojson = brouter.get_route_geojson(points)
        route_feature = geojson["features"][0]
        data_labels = route_feature["properties"]["messages"][0]
        segments = route_feature["properties"]["messages"][1:]
        paths = [dict(zip(data_labels, s)) for s in segments]
        log.debug(paths)
        return paths


if __name__ == "__main__":
    import doctest

    default_router = Router()
    doctest.testmod(extraglobs={"router": default_router})
