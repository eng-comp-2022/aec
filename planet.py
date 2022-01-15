import math
from datetime import datetime, timedelta, timezone


class Planet:
    def __init__(
        self,
        name,
        radius_sun,
        orbital_period: timedelta = timedelta(),
        last_op_earth: datetime = datetime.now(timezone.utc),
    ):
        self.name = name
        self.radius_sun = radius_sun
        self.orbital_period = orbital_period
        self.last_op_earth = last_op_earth

    # returns angle in radians
    def location_angle_earth(self, total_orbiting_duration: timedelta):
        orbit_duration = total_orbiting_duration % self.orbital_period
        percent_complete = orbit_duration / self.orbital_period
        return 2 * math.pi * percent_complete

    # angle in radians
    def distance(self, other, angle):
        # cosine law
        return math.sqrt(
            other.radius_sun ** 2
            + self.radius_sun ** 2
            - 2 * self.radius_sun * other.radius_sun * math.cos(angle)
        )
