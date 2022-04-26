import PySimpleGUI as sg

layout = [
    [sg.Text('Text'), sg.Spin('option', 'options')], 
    [sg.Button('Button')], 
    [sg.Input()],
    [sg.Text('challenge'), sg.Button('challenge')]
]

window = sg.Window('Conversor', layout)


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()