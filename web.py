import streamlit as st

import functions


def add_todo():
    todo_local = st.session_state['new_todo'] +'\n'
    todos.append(todo_local)
    functions.give_todo(todos)
    st.session_state['new_todo'] = ''


# st.html("index.html")
st.title('Todo App')
st.subheader('A Simple interactive todo web app')
st.write('Todos:')

todos = functions.get_todo()

for todo_id, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(todo_id)
        functions.give_todo(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='', placeholder='Add a new todo: ', on_change=add_todo, key='new_todo')
