import math
from datetime import timedelta

light_speed = 299792458  # m/s

seconds_in_day = 86400


def kin_duration(displacement, velocity):
    return displacement / velocity


# angular velocity in rads/second
def angular_velocity(period: timedelta):
    return 2 * math.pi / period.total_seconds()
