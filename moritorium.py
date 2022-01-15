import math

# moratoriam tolerance is 7 degrees; convert to radians
_moritorium_tolerance = 7 * math.pi / 180


def is_moratorium(planet_angle_diff) -> bool:
    """
    Given the angle between two planets, determines if they fall within a
    moratorium.

    :param float planet_angle_diff: The angle between planets, in radians
    """
    return 0 <= planet_angle_diff <= _moritorium_tolerance
