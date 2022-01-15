from datetime import datetime, timezone
import math

from planet import Planet
from moritorium import is_moratorium
from scientific import seconds_in_day


def calculate(
    planet1: Planet, planet2: Planet, calculation_time=datetime(timezone.utc)
):
    # distance between
    planet1_angle = planet1.location_angle_earth(calculation_time)
    planet2_angle = planet2.location_angle_earth(calculation_time)
    angle_diff = math.fabs(planet1_angle - planet2_angle)
    planet_displacement = planet1.distance(planet2, angle_diff)

    # moratorium
    moratorium_occur = is_moratorium(angle_diff)

    # next opposition date
    opp_date = planet1.next_opposition_date(planet2, calculation_time)

    return planet_displacement, moratorium_occur, opp_date
