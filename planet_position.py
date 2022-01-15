import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import pandas as pd

def planet_positions(planet1, planet2, date):
    """
    Leon_K, Leon_KLeon_K 10788 bronze badges, and r-beginners “Animating multiple dots in different orbits in 
    Python using FuncAnimation,” Stack Overflow, 01-Mar-1969. [Online]. 
    Available: https://stackoverflow.com/questions/66341320/animating-multiple-dots-in-different-orbits-in-python-using-funcanimation. 
    [Accessed: 15-Jan-2022].
    """

    plt.style.use("dark_background")

    rad_angle1 = planet1.location_angle_earth(date)
    rad_angle2 = planet2.location_angle_earth(date)

    n_points = 100
    if planet1.orbital_period < planet2.orbital_period:
        theta = np.linspace(rad_angle1, 2 * np.pi * (planet1.orbital_period/planet2.orbital_period)  + rad_angle1, n_points)
        theta_2 = np.linspace(rad_angle2, 2 * np.pi + rad_angle2, n_points)
    else:
        theta = np.linspace(rad_angle1, 2 * np.pi + rad_angle1, n_points)
        theta_2 = np.linspace(rad_angle2, 2 * np.pi * (planet2.orbital_period/planet1.orbital_period) + rad_angle2, n_points)

    if planet1.radius_sun > planet2.radius_sun:
        e_radius = 7
        m_radius = planet2.radius_sun / planet1.radius_sun * 7
    else:
        e_radius = planet1.radius_sun / planet2.radius_sun * 7
        m_radius = 7

    x = e_radius * np.sin(theta)
    y = e_radius * np.cos(theta)

    xx = m_radius * np.sin(theta_2)
    yy = m_radius * np.cos(theta_2)

    fig, ax = plt.subplots(figsize=(5, 5))
    ax = plt.axes(xlim=(-8, 8), ylim=(-8, 8))

    p1, = ax.plot([], [], 'r.', markersize=15)
    p2, = ax.plot([], [], 'g.', markersize=15)
    ax.plot(0, 0, 'X', markersize=5, color="yellow")
    plt.grid(True, lw=0.3)
    ax.plot(x, y, 'r-')
    ax.plot(xx, yy, 'g-')

    def animate(i):
        p1.set_data(x[i], y[i])
        p2.set_data(xx[i], yy[i])
        return p1,p2

    anim = FuncAnimation(fig, animate, frames=1000, interval=200, repeat=False)
    plt.show()
