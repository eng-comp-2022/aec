import math
from datetime import date, datetime, timedelta, timezone

# Class Planet
"""
All angle calculations were done with repect to earth becuase that was given
as a reference point for the periods given.
"""


class Planet:
    def __init__(
        self,
        name,
        radius_sun,
        orbital_period: timedelta = timedelta(),  # orbital adius is taken as a timedelta type
        last_op_earth: datetime = datetime.now(timezone.utc),
    ):
        self.name = name
        self.radius_sun = radius_sun
        self.orbital_period = orbital_period
        self.last_op_earth = last_op_earth

    """
    returns angle in radians of planet with respect to "earth"
    param:
        total_orbiting_duration: total time it has been in orbit
    """

    def location_angle_earth(self, total_orbiting_duration: timedelta):
        # modular math to get position of the current period
        current_orbit_duration = total_orbiting_duration % self.orbital_period
        percent_complete = current_orbit_duration / self.orbital_period
        return 2 * math.pi * percent_complete

    """
    return the next date when the planets are next oppositions
    param:
        calculation_time is the time
    """
    # returns a datetime of the next opposition between the two planets
    def next_opposition_date(self, calculation_time=datetime.now(timezone.utc)):
        total_orbiting_duration = calculation_time - self.last_op_earth
        current_orbit_duration = total_orbiting_duration % self.orbital_period
        return calculation_time + self.orbital_period - current_orbit_duration

    # provide angle diff in radians
    def distance(self, other, planet_angle_diff):
        # cosine law
        return math.sqrt(
            other.radius_sun ** 2
            + self.radius_sun ** 2
            - 2 * self.radius_sun * other.radius_sun * math.cos(planet_angle_diff)
        )

    def abs_angle_diff(self, other, calculation_time: datetime):
        planet1_angle = self.location_angle_earth(calculation_time)
        planet2_angle = other.location_angle_earth(calculation_time)
        angle_diff = math.fabs(planet1_angle - planet2_angle)
        return angle_diff
