from pathlib import Path

DEFAULT_PROFILE_PATH = "vancycling.brf"

BEFORE = """
---context:global
assign validForBikes      = true
assign processUnusedTags  = true
---context:way
"""

AFTER = """
---context:node
assign defaultaccess =
       if ( access= ) then true
       else if ( access=private|no ) then false
       else true
assign bike_access =
       if nodeaccessgranted=yes then true
       else if bicycle= then
       (
         if vehicle= then defaultaccess
         else not vehicle=private|no
       )
       else not bicycle=private|no|dismount
assign footaccess =
       if bicycle=dismount then true
       else if foot= then defaultaccess
       else not foot=private|no
assign initialcost =
       if bike_access then 0
       else ( if footaccess then 10 else 1000000 )
"""


def transpile(router):
    profile_parts = [BEFORE, AFTER]
    return Path(DEFAULT_PROFILE_PATH).read_text()


if __name__ == "__main__":
    from router import Router

    profile = transpile(Router())
    Path(DEFAULT_PROFILE_PATH).write_text(profile)
