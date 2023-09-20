# Vancouver AAA Cycling BRouter Profile

> The City of Vancouver has a vision to make cycling safe, convenient,
> comfortable and fun for All Ages and Abilities (AAA), including families with
> children, seniors, and new riders.
> https://vancouver.ca/files/cov/design-guidelines-for-all-ages-and-abilities-cycling-routes.pdf

Most riders who strongly prefer AAA cycleways will immediately notice they can't
trust their default map apps to suggest nice routes. In Vancouver, common apps
offer distressing suggestions like taking Pender, Robson, even Granville; which
makes getting around by bicycle impractical for many at first, until they
eventually learn that there are longer but welcoming alternatives.

For example, consider searching for a route from Ramen Danbo at Robson to Jam
Café at Beatty.

|             ⠀              |             ⠀              |              ⠀               |
| :------------------------: | :------------------------: | :--------------------------: |
| ![](/docs/case1/gmaps.jpg) | ![](/docs/case1/amaps.jpg) | ![](/docs/case1/brouter.jpg) |

Google Maps suggests going down at Robson - one of the busiest streets in
Downtown Vancouver - until it finally takes protected bike paths at Hornby and
at Smithe, only to move back to Robson! Why not stay on Smithy before turning
left at Beatty? For some reason, Google Maps estimates that going straight at
Smithe up until Beatty St would take 6 more minutes. Maybe they know that
cyclists fearing for their lives will arrive faster? Sometimes Google Maps will
simply suggest going down at Robson all the way towards Beatty St, so it seems
some transient feature (like traffic) is factoring in the routing choices.

Apple maps suggests going down at Robson until it takes a protected bike path at
Hornby; then taking the protected bike path at Dunsmuir. A decent balance of
speed and comfort that an experienced rider would accept, certainly much better
than what Google Maps suggests. But still, 4 blocks of Robson St traffic (about
750 m) is far from AAA, so many riders would be happier if they had a route that
got off of Robson as soon as possible.

The custom profile for BRouter in this repository offers that route: merely 300m
longer but immediately leaving Robson for Jervis and Haro which are residential
streets plus Smithe, Horny and Dunsmuir protected paths. The goal of this
project is researching a routing profile that is highly biased towards pleasant
rides in the Vancouver Metro region.

## Case Study

[brouter]: https://brouter.de/brouter-web/#map=14/49.2853/-123.1407/standard&lonlats=-123.126559,49.289796;-123.097153,49.278784;-123.124914,49.279419;-123.135149,49.291143;-123.156363,49.303125;-123.148831,49.272573

|             ⠀              |             ⠀              |              ⠀               |
| :------------------------: | :------------------------: | :--------------------------: |
| ![](/docs/case2/gmaps.jpg) | ![](/docs/case2/amaps.jpg) | ![](/docs/case2/brouter.jpg) |

## Development

### Build

Until BRouter Web supports permalink/perennial profiles, we need to export the
profile definition files for users to import on their browsers:

```bash
poetry run python vancycling_brouter_profile/transpiler.py
```

This command updates the root `vancycling.brf` profile with the current router.

### Test

Tests always use live definitions, so there's no need to build beforehand.

```bash
poetry run python vancycling_brouter_profile/router.py
```
