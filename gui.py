import functions
from FreeSimpleGUI import Text, Window, InputText, Button

label = Text('Type in a To-Do')
input_box = InputText(tooltip='Enter todo')
button = Button('Add')

my_window = Window('My To-Do App', layout=[[label], [input_box, button]])
my_window.read()
my_window.close()

