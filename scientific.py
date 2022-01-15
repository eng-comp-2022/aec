import math
from datetime import timedelta

<<<<<<< HEAD
# scientific constants

light_speed = 299792458  # m/s
=======
light_speed = 0.299792458  # m/s
>>>>>>> 4a101b376dad67bfcd3a703b7fe60cd3a196f0ce

seconds_in_day = 86400


def travel_duration(displacement: float, velocity: float) -> float:
    """
    Calculates the duration required to travel the given displacment at the
    specified velocity.
    """
    return displacement / velocity


def angular_velocity(period: timedelta) -> float:
    """
    Computes angular velocity for the provided period in rads/second
    """
    return 2 * math.pi / period.total_seconds()
