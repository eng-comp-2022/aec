from datetime import datetime, timezone

from planet import Planet
from moritorium import is_moratorium


def calculate(planet1: Planet, planet2: Planet, calculation_time: datetime):
    angle_diff = planet1.abs_angle_diff(planet2, calculation_time)
    return (
    planet1.displacement(planet2, angle_diff),
    is_moratorium(angle_diff),
    planet1.next_opposition_date(planet2, calculation_time))
