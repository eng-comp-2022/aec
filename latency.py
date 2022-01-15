from datetime import datetime, timedelta
import math

from planet import Planet
from scientific import light_speed, kin_duration

# Computes the latncy between the two planets that are passed 
# in as parameters. The parameter calculation_time is used to provide a relative 
# time value to compute the distance betweent the two planets.
def communication_latency(planet1: Planet, planet2: Planet, calculation_time: datetime):
    angle1 = planet1.location_angle_earth(calculation_time - planet1.last_op_earth)
    angle2 = planet2.location_angle_earth(calculation_time - planet2.last_op_earth)
    angle_diff = math.fabs(angle1 - angle2)
    planet_displacement = planet1.distance(planet2, angle_diff)
    return kin_duration(planet_displacement, light_speed)
