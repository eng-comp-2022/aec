from datetime import datetime, timedelta
import math

from planet import Planet
from scientific import light_speed, kin_duration


def communication_latency(planet1: Planet, planet2: Planet, calculation_time: datetime):
    angle1 = planet1.location_angle_earth(calculation_time - planet1.last_op_earth)
    angle2 = planet2.location_angle_earth(calculation_time - planet2.last_op_earth)
    angle_diff = math.fabs(angle1 - angle2)
    planet_displacement = planet1.distance(planet2, angle_diff)
    return kin_duration(planet_displacement, light_speed)
