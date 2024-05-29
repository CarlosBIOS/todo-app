# FreeSimpleGUI is only able to create desktop GUIs. To make web apps, you need to use a Python web framework. The most
# popular web frameworks are Django, Flask, and Streamlit. In fact, Python is way better for building web apps. We will
# eventually build a To-Do List web app on Day 19!!!
from FreeSimpleGUI import Text, Window, InputText, Button, Listbox

import functions

label = Text('Type in a To-Do')
input_box = InputText(tooltip='Enter todo', key='todo')
add_button = Button('Add')
list_box = Listbox(values=functions.get_and_write_todos(), enable_events=False, size=(45, 10), key='todos')
edit_button = Button('Edit')

my_window = Window('My To-Do App', layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = my_window.read()
    print(event, values)
    match event:
        case 'Add':
            my_window['todos'].update(values=functions.get_and_write_todos(item=values['todo']))

        case 'Edit':
            my_window['todos'].update(values=functions.get_and_write_todos(item=values['todo'],
                                                                           substituir=values['todos'][0]))
            # Ver mais casos, pois ainda dá mal!!!!!

        case WIN_CLOSED:
            break

my_window.close()
