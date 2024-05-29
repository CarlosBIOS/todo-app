FILEPATH = 'Files/todo.txt'


def get_and_write_todos(filepath: str = FILEPATH, item: str = None) -> list:
    """
    Reads the to-do list from a text file, adds a new `item` if provided,
    and writes the updated list back to the file.

    Args:
        filepath (str, optional): The path to the to-do list file. Defaults to 'Files/to-do.txt'.
        item (str, optional): A new to-do `item` to add to the list. Defaults to None.

    Returns:
        list: The updated list of to-do items.
    """

    with open(filepath, 'r+') as file:
        todos: list = file.readlines()  # Read existing todos
        if item:
            todos.append(f'{item}\n')  # Add new item if provided
        file.seek(0)  # Move the pointer to the beginning of the file
        file.writelines(todos)  # Write the updated list back to the file

    return todos
