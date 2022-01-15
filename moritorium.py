import math
# moratoriam tolerance is 7 degrees
_moritorium_tolerance = 7 * math.pi / 180

# calculate whether the 2 panets are in moratoriam.
# provide angle in radians
def is_moratorium(planet_angle_diff):
    return 0 <= planet_angle_diff <= _moritorium_tolerance
