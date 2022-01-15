import math
from datetime import datetime, timedelta, timezone
from scientific import seconds_in_day, angular_velocity

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

    def location_angle_earth(self, calculation_time: datetime):
        """
        returns angle in radians of planet with respect to "earth"
        param:
            total_orbiting_duration: total time it has been in orbit
        """
        # modular math to get position of the current period
        total_orbiting_duration = calculation_time - self.last_op_earth
        total_duration_days = total_orbiting_duration.total_seconds() / seconds_in_day
        orbital_period_days = self.orbital_period.total_seconds() / seconds_in_day
        current_orbit_duration = total_duration_days % orbital_period_days
        percent_complete = current_orbit_duration / orbital_period_days
        return 2 * math.pi * percent_complete

    # returns a datetime of the next opposition between the two planets
    def next_opposition_date(self, other, calculation_time=datetime.now(timezone.utc)):
        planet1_w = angular_velocity(self)
        planet2_w = angular_velocity(other)
        orbit_w = abs(planet1_w - planet2_w)

        # faster planet orbits at relative angular velocity wrt base planet
        base_planet = self
        orbiting_planet = other
        if planet1_w < planet2_w:
            base_planet = other
            orbiting_planet = self

        # current angle of each planet
        orbit_planet_angle = orbiting_planet.location_angle_earth(calculation_time)
        base_planet_angle = base_planet.location_angle_earth(calculation_time)

        # remaining angle in orbit before opposition
        diff_angle = math.fabs(orbit_planet_angle - base_planet_angle)
        angular_displacement = diff_angle
        if orbit_planet_angle > base_planet_angle:
            angular_displacement = 2 * math.pi - diff_angle

        # convert remaining angle to duration
        travel_duration_secs = angular_displacement / orbit_w
        travel_duration = timedelta(seconds=travel_duration_secs)

        # add remaining duration to current time
        return calculation_time + travel_duration

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
