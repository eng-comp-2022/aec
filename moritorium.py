import math

_moritorium_tolerance = 7 * math.pi / 180

# provide angle in radians
def is_moratorium(planet_angle_diff):
    return 0 <= planet_angle_diff <= _moritorium_tolerance
