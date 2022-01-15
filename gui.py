import PySimpleGUI as sg
width = 26

def create_main_layout():
    add_planet_column = [
        [
            sg.Button("Add Planet", size=(15, 1), key="-ADD_PLANET-", font=("Helvetica", 20))
        ]
    ]

    calculate_column = [
        [
            sg.Button("Calculate", size=(15, 1), key="-CALCULATE-", font=("Helvetica", 20)),
        ]
    ]

    layout = [
        [
            sg.Text("Configuration", size=(width, 1), font=("Helvetica", 40),),
        ],
        [
            sg.Text("Planet Name:", size=(width, 1), font=("Helvetica", 20)),
            sg.Input(key="-PLANET_NAME-", size=(10, 1), default_text="Earth", font=("Helvetica", 20))
        ],
        [
            sg.Text("Orbital Radius [in millions km]:", size=(width, 1), font=("Helvetica", 20)),
            sg.Input(key="-ORBITAL_RADIUS-", size=(10, 1), default_text="149.6", font=("Helvetica", 20)),
        ],
        [
            sg.Text("Orbital Period [in Earth days]:", size=(width, 1), font=("Helvetica", 20)),
            sg.Input(key="-ORBITAL_PERIOD-", size=(10, 1), default_text="365.24", font=("Helvetica", 20))
        ],
        [
            sg.Text("Date of Last Opposition with Earth:", size=(width, 1), font=("Helvetica", 20)),
        ],
        [
            sg.Text("Year:", size=(4, 1), font=("Helvetica", 20)),
            sg.Combo([x for x in list(range(1922, 2023))], font=("Helvetica", 20), key='-LAST_YEAR-', readonly=True),
            sg.Text("Month:", size=(5, 1), font=("Helvetica", 20)),
            sg.Combo([x for x in list(range(1, 13))], font=("Helvetica", 20), key='-LAST_MONTH-', readonly=True),
            sg.Text("Day:", size=(4, 1), font=("Helvetica", 20)),
            sg.Combo([x for x in list(range(1, 32))], font=("Helvetica", 20), key='-LAST_DAY-', readonly=True),
            sg.Text("Hour:", size=(4, 1), font=("Helvetica", 20)),
            sg.Combo([x for x in list(range(0, 24))], font=("Helvetica", 20), key='-LAST_HOUR-', readonly=True),
            sg.Text("Minute:", size=(6, 1), font=("Helvetica", 20)),
            sg.Combo([x for x in list(range(0, 60))], font=("Helvetica", 20), key='-LAST_MINUTE-', readonly=True),
            sg.Text("Second:", size=(6, 1), font=("Helvetica", 20)),
            sg.Combo([x for x in list(range(0, 60))], font=("Helvetica", 20), key='-LAST_SECOND-', readonly=True),
        ],
        [
            sg.Column(add_planet_column, element_justification='right', expand_x=True)
        ],
        [
            sg.Text("_"*150)
        ],
        [
            sg.Text("Calculcation", size=(width, 1), font=("Helvetica", 40),),
        ],
        [
            sg.Text("Planet 1:", size=(10, 1), font=("Helvetica", 20)),
            sg.Combo(['         '], font=("Helvetica", 20), key='-PLANET_1-', readonly=True),
        ],
        [
            sg.Text("Planet 2:", size=(10, 1), font=("Helvetica", 20)),
            sg.Combo(['         '], font=("Helvetica", 20), key='-PLANET_2-', readonly=True),
        ],
        [
            sg.Text("Earth date for Calculations:", size=(20, 1), font=("Helvetica", 20)),
        ],
        [
            sg.Text("Year:", size=(4, 1), font=("Helvetica", 20)),
            sg.Combo([x for x in list(range(2022, 2123))], font=("Helvetica", 20), key='-TIME_YEAR-', readonly=True),
            sg.Text("Month:", size=(5, 1), font=("Helvetica", 20)),
            sg.Combo([x for x in list(range(1, 13))], font=("Helvetica", 20), key='-TIME_MONTH-', readonly=True),
            sg.Text("Day:", size=(4, 1), font=("Helvetica", 20)),
            sg.Combo([x for x in list(range(1, 32))], font=("Helvetica", 20), key='-TIME_DAY-', readonly=True),
            sg.Text("Hour:", size=(4, 1), font=("Helvetica", 20)),
            sg.Combo([x for x in list(range(0, 24))], font=("Helvetica", 20), key='-TIME_HOUR-', readonly=True),
            sg.Text("Minute:", size=(6, 1), font=("Helvetica", 20)),
            sg.Combo([x for x in list(range(0, 60))], font=("Helvetica", 20), key='-TIME_MINUTE-', readonly=True),
            sg.Text("Second:", size=(6, 1), font=("Helvetica", 20)),
            sg.Combo([x for x in list(range(0, 60))], font=("Helvetica", 20), key='-TIME_SECOND-', readonly=True),
        ],
        [
            sg.Column(calculate_column, element_justification='right', expand_x=True)
        ],
    ]

    return layout


def create_result_layout(image, dist_between,morat,next_opp,seconds,date):
    position_column = [
        [
            sg.Button("Planet Positions", size=(15, 1), key="-PLANET_POSITION-", font=("Helvetica", 20)),
        ]
    ]

    layout = [
        [
            sg.Text("Results", size=(width, 1), font=("Helvetica", 40))
        ],
        [
            sg.Text("Time vs. Latency over the next 48 months", size=(36, 1), font=("Helvetica", 25))
        ],
        [
            sg.Image(key="-IMAGE-", data=image)
        ],
        [
            sg.Text("_"*100)
        ],
        [
            sg.Text("On: " + date.strftime("%Y-%m-%d"), size=(width, 1), font=("Helvetica", 30)),
        ],
        [
            sg.Text("Distance: " + str(dist_between)[:8] + " million kms", font=("Helvetica", 20))
        ],
        [
            sg.Text("Moratorium: " + str(morat), font=("Helvetica", 20)),
        ],
        [
            sg.Text("Latency: " + str(seconds[0])[:8] + " seconds", font=("Helvetica", 20)),
        ],
        [
            sg.Text("Date of Next Opposition: " + str(next_opp)[:-4], font=("Helvetica", 20)),
        ],
        [
            sg.Column(position_column, element_justification='right', expand_x=True)
        ],

    ]
    return layout