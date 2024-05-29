FILEPATH = 'Files/todo.txt'


def get_and_write_todos(filepath: str = FILEPATH, item: str = None, substituir: str = None) -> list:
    """
    Reads the to-do list from a text file, adds a new `item` if provided,
    and writes the updated list back to the file.

    :param filepath: The path to the to-do list file. Defaults to 'Files/to-do.txt'
    :param item: A new to-do `item` to add to the list. Defaults to None.
    :param substituir: The `item` que quero substituir
    :return: The updated list of to-do items
    """

    with open(filepath, 'r+') as file:
        todos: list = file.readlines()  # Read existing todos
        if item:
            index = len(todos)
            if substituir:
                index = todos.index(substituir)
                todos.remove(substituir)
            todos.insert(index, f'{item}\n')  # Add new item if provided
        file.seek(0)  # Move the pointer to the beginning of the file
        file.writelines(todos)  # Write the updated list back to the file

    return todos
