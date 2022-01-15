from datetime import datetime, timezone

from planet import Planet
from moritorium import is_moratorium
from scientific import seconds_in_day


def calculate(planet1: Planet, planet2: Planet, calculation_time=datetime.utcnow()):
    # distance between
    angle_diff = planet1.abs_angle_diff(planet2, calculation_time)
    planet_displacement = planet1.distance(planet2, angle_diff)

    # moratorium
    moratorium_occur = is_moratorium(angle_diff)

    # next opposition date
    opp_date = planet1.next_opposition_date(planet2, calculation_time)

    return planet_displacement, moratorium_occur, opp_date
