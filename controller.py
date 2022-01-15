import traceback
import plotly.graph_objects as go
import PySimpleGUI as sg
import datetime

from latency import communication_latency
from dateutil.relativedelta import *
from planet import Planet
from planet_position import planet_positions
from gui import create_main_layout, create_result_layout
from calculator import calculate
from plot import Plot

def open_result_page(dist_between, morat, next_opp, date, planet1, planet2):
    """
    Create line plot for latency between the two planets.
    """
    example_plot = Plot(size=550)

    seconds = []
    dates = []
    for i in range(48):
        seconds.append(
            communication_latency(
                planet1=planet1, planet2=planet2, calculation_time=date
            )
        )
        dates.append(date)
        date = date + relativedelta(months=+1)

    N = 48
    t = dates
    y = seconds

    example_plot.figure = go.Figure(data=go.Scatter(x=t, y=y, mode="lines+markers"))

    result_window = sg.Window(
        "Result Page",
        create_result_layout(
            example_plot.get_image(), dist_between, morat, next_opp, seconds, dates[0]
        ),
    )

    while True:  # Event Loop
        event, values = result_window.read(timeout=100)  # milliseconds

        if event == sg.TIMEOUT_EVENT:
            result_window.refresh()

        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "-PLANET_POSITION-":
            planet_positions(planet1,planet2, dates[0]) # give data

def main():
    planets = {}
    window = sg.Window(
        "Distance and Latency Tool",
        create_main_layout(),
    )

    while True:  # Event Loop
        event, values = window.read(timeout=100)  # milliseconds

        if event == sg.TIMEOUT_EVENT:
            window.refresh()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-ADD_PLANET-":
            try:
                date = datetime.datetime(
                    int(values["-LAST_YEAR-"]),
                    int(values["-LAST_MONTH-"]),
                    int(values["-LAST_DAY-"]),
                    int(values["-LAST_HOUR-"]),
                    int(values["-LAST_MINUTE-"]),
                    int(values["-LAST_SECOND-"]),
                )  # validate time
                planet = Planet(
                    values["-PLANET_NAME-"],
                    float(values["-ORBITAL_RADIUS-"]),
                    datetime.timedelta(days=float(values["-ORBITAL_PERIOD-"])),
                    date,
                )
                planets[values["-PLANET_NAME-"]] = planet
                window["-PLANET_1-"].update(values=[x for x in planets.keys()])
                window["-PLANET_2-"].update(values=[x for x in planets.keys()])
            except Exception as e:
                sg.popup_error(f"Invalid Input.")
                print(e)
        if event == "-CALCULATE-":
            try:
                date = datetime.datetime(
                    int(values["-TIME_YEAR-"]),
                    int(values["-TIME_MONTH-"]),
                    int(values["-TIME_DAY-"]),
                    int(values["-TIME_HOUR-"]),
                    int(values["-TIME_MINUTE-"]),
                    int(values["-TIME_SECOND-"]),
                )  # validate time
                if values["-PLANET_1-"] != values["-PLANET_2-"]:
                    dist_between, morat, next_opp = calculate(
                        planets[values["-PLANET_1-"]],
                        planets[values["-PLANET_2-"]],
                        date,
                    )
                    open_result_page(
                        dist_between,
                        morat,
                        next_opp,
                        date,
                        planets[values["-PLANET_1-"]],
                        planets[values["-PLANET_2-"]],
                    )
                else:
                    sg.popup_error(f"Please choose two distinct planets.")
            except Exception as e:
                sg.popup_error(f"Invalid Input.")
                tb = traceback.format_exc()
                sg.Print(f"An error happened.  Here is the info:", e, tb)
                print(e)

    window.close()
