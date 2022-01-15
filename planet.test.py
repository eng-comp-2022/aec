from planet import Planet
import datetime
import math

earth = Planet("paul", radius_sun=10)
mercury = Planet("paul", 5, orbital_period=datetime.timedelta(days=10))
pluto = Planet("paul", 50, orbital_period=datetime.timedelta(days=100))

print(earth.displacement(mercury, math.pi / 2))  # 11.18
print(earth.displacement(mercury, math.pi))  # 15
print(earth.displacement(pluto, math.pi / 2))  # 50.99
print(earth.displacement(pluto, math.pi))  # 60

# TODO: implement real unit test

total_orbiting_duration = datetime.timedelta(days=5)
print(mercury.location_angle_earth(total_orbiting_duration))

total_orbiting_duration = datetime.timedelta(days=20)
calculate_time = pluto.last_op_earth + total_orbiting_duration
print(pluto.location_angle_earth(calculate_time))

total_orbiting_duration = datetime.timedelta(days=220)
calculate_time = pluto.last_op_earth + total_orbiting_duration
print(pluto.location_angle_earth(calculate_time))

total_orbiting_duration = datetime.timedelta(days=-5)
calculate_time = mercury.last_op_earth + total_orbiting_duration
print(mercury.location_angle_earth(calculate_time))
