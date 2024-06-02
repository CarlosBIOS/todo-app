# Informações sobre streamlit:
# O que é Streamlit?
# O Streamlit é uma biblioteca Python de código aberto que permite criar aplicativos web interativos de forma rápida e
# fácil. Ele é especialmente projetado para cientistas de dados e engenheiros de machine learning. Com o Streamlit,
# é possível transformar os seus scripts Python em aplicativos web interativos em minutos, sem a necessidade de escrever
# nenhum código HTML, CSS ou JavaScript. O Streamlit fornece uma série de widgets e funções que permitem criar
# interfaces de usuário atraentes e fáceis de usar.

# Nota: para executar o código, não pode ser aqui e sim no terminal e tenho que escrever:
# streamlit run web.py

import streamlit as st
from functions import get_and_write_todos
from os import path


def add_todo():
    novo_todo = st.session_state['new_todo'] + '\n'
    todos.append(novo_todo)
    get_and_write_todos(item=novo_todo)


if not path.exists('todo_done.txt'):
    with open('todo_done.txt', 'w') as output_file:
        pass

if not path.exists('todo.txt'):
    with open('todo.txt', 'w') as output_file:
        pass

todos = get_and_write_todos()
todos_complete = get_and_write_todos(filepath='todo_done.txt')

st.title('My todo App')
st.subheader('')
# st.subheader('This is my to-do App')
# st.write('This app is to increse your product')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        get_and_write_todos(remove_item=todo)
        del todos[index]
        del st.session_state[todo]
        get_and_write_todos(filepath='todo_done.txt', item=todo)
        todos_complete.append(todo)
        st.rerun()

# for index, to-do in enumerate(todos_complete):
#     checkbox = st.checkbox(to-do, key=to-do)

st.text_input(label='', placeholder='Add a new todo', on_change=add_todo, key='new_todo')

st.session_state
