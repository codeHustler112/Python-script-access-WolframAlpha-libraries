import PySimpleGUI as sg
import wolframalpha
from wolframalpha import Client


app_id = '*******************'
client = wolframalpha.Client(app_id)




sg.theme('DarkAmber')	# Add a touch of color
# All the stuff inside your window.
layout = [  
            [sg.Text('Enter your Question'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('zama', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
    res = client.query(values[0])
    sg.popup(next(res.results).text)

    

window.close()

