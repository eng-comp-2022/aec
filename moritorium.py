import math

_moritorium_tolerance = 7 * math.pi / 180

# provide angle in radians
def is_moratorium(planet1_angle, planet2_angle):
    angle_diff = math.fabs(planet1_angle - planet2_angle)
    return 0 <= angle_diff <= _moritorium_tolerance
