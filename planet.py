import math
from datetime import datetime, timedelta, timezone
from scientific import angular_velocity


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

    # returns angle in radians of planet with respect to earth
    def location_angle_earth(self, calculate_time: datetime):
        """ballsack"""
        total_orbiting_duration = calculate_time - self.last_op_earth
        current_orbit_duration = total_orbiting_duration % self.orbital_period
        percent_complete = current_orbit_duration / self.orbital_period
        return 2 * math.pi * percent_complete

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
