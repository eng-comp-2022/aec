import traceback
import plotly.graph_objects as go
import numpy as np
import PySimpleGUI as sg
import datetime

from planet import Planet
from gui import create_main_layout, create_result_layout
from calculator import calculate, calculate_with_earth
from plot import Plot

def open_result_page(dist_between,morat,next_opp,lat_list,date):    
    example_plot = Plot(size=700)
    
    N = 1000
    t = np.linspace(0, 10, 100)
    y = np.sin(t)

    example_plot.figure = go.Figure(data=go.Scatter(x=t, y=y, mode='markers'))

    result_window = sg.Window("Result Page", create_result_layout(example_plot.get_image(),dist_between,morat,next_opp,lat_list,date))

    while True:  # Event Loop
        event, values = result_window.read(timeout=100)  # milliseconds

        if event == sg.TIMEOUT_EVENT:
            result_window.refresh()
        
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

def main():
    planets = {}
    window = sg.Window("Distance and Latency Tool", create_main_layout(),)

    while True:  # Event Loop
        event, values = window.read(timeout=100)  # milliseconds

        if event == sg.TIMEOUT_EVENT:
            window.refresh()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-ADD_PLANET-":
            try:
                date = datetime.datetime(int(values["-LAST_YEAR-"]), int(values["-LAST_MONTH-"]), int(values["-LAST_DAY-"])) # validate time
                planet = Planet(values["-PLANET_NAME-"], float(values["-ORBITAL_RADIUS-"]), datetime.timedelta(days=float(values["-ORBITAL_PERIOD-"])), date)
                planets[values["-PLANET_NAME-"]] = planet
                window["-PLANET_1-"].update(values = [x for x in planets.keys()])
                window["-PLANET_2-"].update(values = [x for x in planets.keys()])
            except Exception as e:
                sg.popup_error(f'Invalid Input.')
        if event == "-CALCULATE-": 
            try:
                date = datetime.datetime(int(values["-TIME_YEAR-"]), int(values["-TIME_MONTH-"]), int(values["-TIME_DAY-"])) # validate time
                if (values["-PLANET_1-"] != values["-PLANET_2-"]):
                    if "Earth" in {values["-PLANET_1-"], values["-PLANET_2-"]}:
                        dist_between,morat,next_opp,lat_list = calculate(planets[values["-PLANET_1-"]], planets[values["-PLANET_2-"]])
                    else:
                        dist_between,morat,next_opp,lat_list = calculate_with_earth(planets[values["-PLANET_1-"]], planets[values["-PLANET_2-"]], planets["Earth"])

                    open_result_page(dist_between,morat,next_opp,lat_list,date)
                else:
                    sg.popup_error(f'Please choose two distinct planets.')
            except Exception as e:
                sg.popup_error(f'Invalid Input.')
                tb = traceback.format_exc()
                sg.Print(f'An error happened.  Here is the info:', e, tb)
                print(e)

    window.close()