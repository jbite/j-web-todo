import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.wFile(todos=todos)

todos = functions.showTodos()
st.title("My Todo App")
st.subheader("This is my todo App.")
st.write("This app is to increase your productivity.")


for i,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=i)
    if checkbox:
        todos.pop(i)
        functions.wFile(todos=todos)
        del st.session_state[i]
        st.rerun()

st.text_input(label="Todo", placeholder="Add new todo...", 
                on_change=add_todo, key='new_todo')


# st.session_state