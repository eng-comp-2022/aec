import math
from datetime import datetime, timedelta, timezone
from scientific import angular_velocity, duration_in_days


class Planet:
    """
    Represents a planet, and provides operations on it.
    """

    def __init__(
        self,
        name: str,
        radius_sun: float,
        orbital_period: timedelta = timedelta(),
        last_op_earth: datetime = datetime.now(timezone.utc),
    ):
        self.name = name
        self.radius_sun = radius_sun
        self.orbital_period = orbital_period
        self.last_op_earth = last_op_earth

    def location_angle_earth(self, calculation_time: datetime) -> float:
        """
        returns angle in radians of planet with respect to 'earth'
        param datetime calculation_time: time at which angle should be calculated
        """

        # compute orbital durations in days
        total_orbiting_duration = calculation_time - self.last_op_earth
        total_orbiting_duration_days = duration_in_days(total_orbiting_duration)
        orbital_period_days = duration_in_days(self.orbital_period)

        # modular math to get position of planet in the current period
        current_orbit_duration = total_orbiting_duration_days % orbital_period_days
        percent_complete = current_orbit_duration / orbital_period_days
        return 2 * math.pi * percent_complete

    # returns a datetime of the next opposition between the two planets
    def next_opposition_date(
        self, other: "Planet", calculation_time: datetime
    ) -> datetime:
        """
        With respect to the given calculation time, computes the next date at
        which planetary opposition will occur between self the the provided
        other planet.
        """
        planet1 = self
        planet2 = other
        planet1_w = angular_velocity(planet1.orbital_period)
        planet2_w = angular_velocity(planet2.orbital_period)

        # choose faster planet to orbit at relative angular velocity w.r.t. base planet
        if planet1_w < planet2_w:
            base_planet, orbiting_planet, orbit_w = planet2, planet1, planet1_w
        else:
            base_planet, orbiting_planet, orbit_w = planet1, planet2, planet2_w

        # current angle of each planet
        orbit_planet_angle = orbiting_planet.location_angle_earth(calculation_time)
        base_planet_angle = base_planet.location_angle_earth(calculation_time)

        # remaining angle in orbit to reach opposition; to reach the base planet
        diff_angle = math.abs(base_planet_angle - orbit_planet_angle)
        angular_displacement = diff_angle
        if orbit_planet_angle > base_planet_angle:
            angular_displacement = 2 * math.pi - diff_angle

        # convert remaining angle to duration
        travel_duration_days = angular_displacement / orbit_w
        travel_duration = timedelta(days=travel_duration_days)

        # add remaining duration to current time
        return calculation_time + travel_duration

    def distance(self, other: "Planet", planet_angle_diff: float) -> float:
        """
        Computes the distance between the self planet and the other given
        planet, when there is an angle of planet_angle_diff between them.

        :param float planet_angle_diff: the angle between the two planets, in radians
        """
        # calculate opposite side of triangle created between two planets and
        # sun using cosine law
        return math.sqrt(
            other.radius_sun ** 2
            + self.radius_sun ** 2
            - 2 * self.radius_sun * other.radius_sun * math.cos(planet_angle_diff)
        )

    def abs_angle_diff(self, other: "Planet", calculation_time: datetime) -> float:
        """
        Calculates the angle, in radians, that will subtend the self planet and
        the other given planet at the provided calculation_time
        """
        planet1_angle = self.location_angle_earth(calculation_time)
        planet2_angle = other.location_angle_earth(calculation_time)
        angle_diff = math.fabs(planet1_angle - planet2_angle)
        return angle_diff
