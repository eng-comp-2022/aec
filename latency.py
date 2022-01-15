from datetime import datetime, timedelta

from planet import Planet
from scientific import light_speed, kin_duration


def communication_latency(planet1: Planet, planet2: Planet, calculation_time: datetime):
    angle_diff = planet1.abs_angle_diff(planet2, calculation_time)
    planet_displacement = planet1.distance(planet2, angle_diff)
    return kin_duration(planet_displacement, light_speed)
