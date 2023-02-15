import PySimpleGUI as sg

#create a new layout
def create_new_task():
    sg.theme('DarkBlue4') #theme's name
    line = [
        [sg.Checkbox(''), sg.Input('')] #a checkbox and a input box in the same line
    ]
    layout = [
        [sg.Frame('Tarefas', layout=line, key='container')],
        [sg.Button('Nova Tarefa'), sg.Button('Limpar')]
    ]

    return sg.Window('Todo List', layout=layout, finalize=True)

# create the window
window = create_new_task()

#create the window's rules

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break