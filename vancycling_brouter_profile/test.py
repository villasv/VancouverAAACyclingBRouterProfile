from typing import List, Optional
from collections import namedtuple
from pathlib import Path

import logging
import brouter

DEFAULT_PROFILE_PATH = "vancycling.brf"

LonLat = namedtuple("LonLat", "lon lat")


class Router:
    def __init__(self, profile_spec: Optional[str] = None):
        if profile_spec is None:
            profile_spec = Path(DEFAULT_PROFILE_PATH).read_text()

        self.profile = profile_spec

    def _pedestrian_penalty(self, **context):
        """
        Avoid pedestrian infrastructure, but not too much! The bicycle is the
        only vehicle that can be carried around by foot in pedestrian paths,
        it's a very useful feature.

        Lost Lagoon to Rawlings Trail: should take the small pedestrian bridge.
        This pedestrian-only section is very small and has low foot traffic, and
        it connects two adjacent bike paths. The alternative would be taking the
        Stanley Park Seawall Bike Path around Ceperley Meadow, but the
        difference in distance is not worth it.

        >>> ll, rt = LonLat(-123.145752, 49.295477), LonLat(-123.150858,49.296597)
        >>> router.eval([ll, rt])


        # Adjust based on: # - Third Beach to Second Beach (should prefer
        Seawall) # - Seaside Path vs Beach Avenue Lane #
        https://brouter.de/brouter-web/#map=15/49.2898/-123.1474/standard&lonlats=-123.150913,49.296269;-123.135583,49.277691
        # - Convention Center stairs vs Seawall lane

        """
        return

    def eval(self, points: List[LonLat]):
        brouter.get_route()


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"router": Router()})
