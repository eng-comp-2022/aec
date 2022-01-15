from planet import Planet
import math
from datetime import timedelta
from scientific import light_speed
from latency import communication_latency

mercury = Planet("paul", 5, orbital_period=timedelta(days=10))
pluto = Planet(
    "paul", 50, orbital_period=timedelta(days=100), last_op_earth=mercury.last_op_earth
)

print(math.fabs(50 - 5) / light_speed)
print(communication_latency(mercury, pluto, mercury.last_op_earth))
