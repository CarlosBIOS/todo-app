# FreeSimpleGUI is only able to create desktop GUIs. To make web apps, you need to use a Python web framework. The most
# popular web frameworks are Django, Flask, and Streamlit. In fact, Python is way better for building web apps. We will
# eventually build a To-Do List web app on Day 19!!!
from FreeSimpleGUI import Text, Window, InputText, Button
import functions

label = Text('Type in a To-Do')
input_box = InputText(tooltip='Enter todo')
button = Button('Add')

my_window = Window('My To-Do App', layout=[[label], [input_box, button]])
my_window.read()
my_window.close()
