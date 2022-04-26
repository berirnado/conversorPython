import PySimpleGUI as sg

layout = [
    [sg.Input(key = '-INPUT-'), sg.Spin(['km para milhas', 'kg para libras', 'seg para min'], key = '-UNITS-'), sg.Button('Converter', key = '-CONVERT-')], 
    [sg.Text('output', key = '-OUTPUT-')]
]

window = sg.Window('Conversor', layout)


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'km para milhas':
                    output = round(float(input_value) *  0.6214,2)
                    output_string = f'{input_value} km são {output} milhas'
                case 'kg para libras':
                    output = round(float(input_value) * 2.205,2)
                    output_string = f'{input_value} kg são {output} libras'
                case 'seg para min':
                    output = round(float(input_value) / 60,2)
                    output_string = f'{input_value} segundos são {output} minutos'
            window['-OUTPUT-'].update(output_string)
        else: 
            window['-OUTPUT-'].update('Por favor insira um número válido')
window.close()