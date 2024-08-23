def get_todo():
    with open("todos.txt", "r") as f:
        todos_local = f.readlines()

    return todos_local


def give_todo(todo_arg):
    with open("todos.txt", "w") as f:
        f.writelines(todo_arg)
