from datetime import datetime

from planet import Planet
from scientific import light_speed, travel_duration


def communication_latency(
    planet1: Planet, planet2: Planet, calculation_time: datetime
) -> float:
    """
    Computes the communication latency between the two provided planets,
    calculated at the given calculation time.
    """
    angle_diff = planet1.abs_angle_diff(planet2, calculation_time)
    planet_distance = planet1.distance(planet2, angle_diff)
    return travel_duration(planet_distance, light_speed)
