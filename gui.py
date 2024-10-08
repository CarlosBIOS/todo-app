# FreeSimpleGUI is only able to create desktop GUIs. To make web apps, you need to use a Python web framework. The most
# popular web frameworks are Django, Flask, and Streamlit. In fact, Python is way better for building web apps. We will
# eventually build a To-Do List web app on Day 19!!!

# TODO: Como criar um programa que seja executável no windows:
#  1 passo: Verificar se estou neste path no terminal:
#  (.venv) C:\Users\cmmon\Desktop\Estudar\Python\Mega Course\Application 1
#  2 passo: Escrever isto no terminal: pyinstaller --onefile --windowed gui.py
#  Muito Importante: Só posso criar apps para o meu OS!!! No ep.179 mostra para os outros OS!!!!

from FreeSimpleGUI import Text, Window, InputText, Button, Listbox, popup, theme, WINDOW_CLOSED
import functions
import time
import os

if not os.path.exists('todo.txt'):
    with open('todo.txt', 'w') as output_file:
        pass

theme('PythonPlus')
clock = Text('', key='clock')
label = Text('Type in a To-Do')
input_box = InputText(tooltip='Enter todo', key='todo')
# Como acrescantava fotos ao butão, mas o problema que fica muito pequeno:
# complete_button = Button(size=20, image_source='Files/complete.png', mouseover_colors='LightBlue2', key='Complete')
# add_button = Button(size=30, image_source='Files/add.png', mouseover_colors='LightBlue2', tooltip='Add to-do',
#                     key='Add')
add_button = Button('Add')
list_box = Listbox(values=functions.get_and_write_todos(), enable_events=False, size=(45, 10), key='todos')
edit_button = Button('Edit')
exit_button = Button('Exit')
complete_button = Button('Complete')

my_window = Window('My To-Do App',
                   layout=[[clock], [label], [input_box, add_button], [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = my_window.read(timeout=200)
    my_window['clock'].update(value=time.strftime('%d %b %Y, %H:%M:%S'))
    match event:
        case 'Add':
            if values['todo']:
                item = functions.get_and_write_todos(item=values['todo'] + '\n')
                my_window['todos'].update(values=item)
                # Quando escrevo my_window[key] significa que estão a chamar a função, ou seja, my_window['todos']
                # representa ListBox(button) widget
            else:
                popup('Please, escreve algo na caixa de texto para adicioná-lo!', font=('Helvica', 20))

        case 'Edit':
            if values['todo']:
                item = functions.get_and_write_todos(item=values['todo'] + '\n', substituir=values['todos'][0])
                my_window['todos'].update(values=item)
            else:
                popup('Please escolhe uma da lista!', font=('Helvica', 20))

        case 'Complete':
            try:
                todo_to_complete = functions.get_and_write_todos(remove_item=values['todos'][0])
                print(todo_to_complete)
                my_window['todos'].update(values=todo_to_complete)
            except IndexError:
                popup('Please ecolhe um da lista!', font=('Helvica', 20))

        case 'Exit':
            exit()  # Vantagem de usar esta função, é que dps de executá-la, o programa fecha-se completamente, então já
            # não é preciso o my_window.close()

# Acrscentar as que já foram feitas!
# datas
