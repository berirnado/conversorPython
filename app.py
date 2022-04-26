import PySimpleGUI as sg

layout = [
    [sg.Text('Text'), sg.Spin('option', 'options')], 
    [sg.Button('Button')], 
    [sg.Input()],
    [sg.Text('Test'), sg.Button('Test Button')]
]

window = sg.Window('Conversor', layout)


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Button':
        print('button pressed')

    if event == 'Test Button':
        print('Test Button pressed')

window.close()