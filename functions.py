# Fazer uma função onde faz o get_todo e write_todo simultaneamente!!
FILEPATH = 'Files/todo.txt'


def get_todos(filepath: str = FILEPATH, item: str = None) -> list:
    """
    Read a text file and return the list of to-do items.

    If `item` is define, então vão colocá-la na lista of to-do
    :param filepath: O ficheiro txt que quero ler
    :param item:
    :return: a list onde cada elemento é um parágrafo
    """
    with open(filepath) as file_local:
        todos_local: list = file_local.readlines()
        if item:
            todos_local.append(item)
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH) -> None:
    """
    Write the to-do items list in the text files
    :param todos_arg: The items that I want to put in the `filepath`
    :param filepath: O ficheiro onde quero escrever
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
