import streamlit as st

st.title("To-do App")

class Todo:
    def __init__(self, task: str, done: bool = False):
        self.__task = task
        self.__done = done

    def get_task(self):
        return self.__task

    def get_done(self):
        return self.__done

    def set_done(self, done: bool):
        self.__done = done

    def __repr__(self):
        return f"Task: {self.__task}, Done: {self.__done}"

def add_todo():
    task = st.session_state.get("new_task", "").strip()
    if not task:
        return
    st.session_state["todos"].append(Todo(task))
    st.session_state["new_task"] = ""

def toggle_done(index: int):
    key = f"done_{index}"
    st.session_state["todos"][index].set_done(st.session_state[key])

if "todos" not in st.session_state:
    st.session_state["todos"] = []

st.text_input("새로운 할일 추가", key="new_task", on_change=add_todo)

if st.session_state["todos"]:
    for i, todo in enumerate(st.session_state["todos"]):
        key = f"done_{i}"
        if key not in st.session_state:
            st.session_state[key] = todo.get_done()

        col1, col2 = st.columns([0.1, 0.9])
        col1.checkbox(f"{i + 1}", key=key, on_change=toggle_done, args=(i,))
        col2.markdown(f"~~{todo.get_task()}~~" if todo.get_done() else todo.get_task())
else:
    st.info("할일을 추가해 보세요.")
