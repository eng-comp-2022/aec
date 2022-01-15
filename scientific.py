import math
from datetime import timedelta

# scientific constants

light_speed = 299792458  # m/s

seconds_in_day = 86400

def duration_in_days(duration: timedelta) -> float:
    return duration.total_seconds() / seconds_in_day


def travel_duration(displacement: float, velocity: float) -> float:
    """
    Calculates the duration required to travel the given displacment at the
    specified velocity.
    """
    return displacement / velocity


def angular_velocity(period: timedelta) -> float:
    """
    Computes angular velocity for the provided period in rads/day
    """
    return 2 * math.pi / duration_in_days(period)
