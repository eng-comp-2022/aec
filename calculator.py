from datetime import datetime, timezone
from planet import Planet


def calculate(
    planet1: Planet, planet2: Planet, calculation_time=datetime(timezone.utc)
):
    planet1_angle = planet1.location_angle_earth(calculation_time)
    planet2_angle = planet2.location_angle_earth(calculation_time)

    planet_displacement = planet1.distance(
        planet2,
    )
    # distance between
    # weird zone
    # next opposition in days
    #
    return 1, True, 1, [1, 2]
