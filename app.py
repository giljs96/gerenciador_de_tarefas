import PySimpleGUI as sg


def create_new_task():
    sg.theme('LightGrey3')  # theme's name
    line = [
        [sg.Checkbox(''), sg.Input('')]  # a checkbox and a data
        # input fild in the same line
    ]
    layout = [  # create a new layout
        [sg.Frame('Tasks', layout=line, key='container')],
        [sg.Button('New Task'), sg.Button('Reset')]
    ]

    return sg.Window('Task Manager', layout=layout, finalize=True)  # window's title and the app's layout


# create the window
window = create_new_task()

# create the window's rules
while True:
    """ this repetition structure will read the information from that window and
     will store the events (every click made inside the screen) inside this "event" variable
     and the values (everything that is filled in some field) inside the variable "values" """
    event, values = window.read()
    if event == sg.WIN_CLOSED: 
        break
    elif event == 'New Task':
        window.extend_layout(window['container'], [[sg.Checkbox(''), sg.Input('')]])
    elif event == 'Reset':
        window.close()
        window = create_new_task()
