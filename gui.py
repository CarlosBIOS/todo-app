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
exit_button = Button('Exit')
complete_button = Button('Complete')

my_window = Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button, complete_button], [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = my_window.read()
    print(event, values)
    match event:
        case 'Add':
            item = functions.get_and_write_todos(item=values['todo'] + '\n')
            my_window['todos'].update(values=item)
            # Quando escrevo my_window[key] significa que estão a chamar a função, ou seja, my_window['todos']
            # representa ListBox(button) widget

        case 'Edit':
            item = functions.get_and_write_todos(item=values['todo'] + '\n', substituir=values['todos'][0])
            my_window['todos'].update(values=item)
            # Ver mais casos, pois ainda dá mal!!!!!

        case 'Complete':
            todo_to_complete = functions.get_and_write_todos(remove_item=values['todos'][0])
            print(todo_to_complete)
            my_window['todos'].update(values=todo_to_complete)

        case 'Exit':
            exit()  # Vantagem de usar esta função, é que dps de executá-la, o programa fecha-se completamente, então já
            # não é preciso o my_window.close()

        case WIN_CLOSED:
            exit()
