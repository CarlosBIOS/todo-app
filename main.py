# Explicação de como usar o git:
# Primeiramente, para um project ter a funcionalidade do git, temos que ir à opção VSC e escolher a 1 opção!!!!
# Vai à opção master na parte superior esquerdo e carregas em commit. De seguida, escreves no quadrado inferior Initial
# commit e tenho que selecionar os respetivos arquivos no quadrado superior!
# E pronto, agora os ficheiros selecionados vão estar a ser rastreados pelo git!!!!

# Posso escrescentar git checkout e git reset. O git checkout serve para visualizar os ficheiros anteriores, ou seja, se
# eu quisesse voltar para o "passado"(ver a versão anterior), carregava alt+9 selecionava, por exemplo, o ficheiro
# initial commit e com o botão direito do rato carregava checkout revision!! E pronto, estava na versão anterior, e se
# quisesse voltar ao ficheiro mais recente, tinha que carrega nesse mesmo folder e carregar na opção checkout e dps
# master. Mas não se recomenda usar esta opção se realmente quero ir para aquela versão e eliminar permanentemente as
# outras após dessa e sim o git reset. Para acessar ao git reset, é o mesmo processo que git checkout, mas tenho que
# selecionar com o botão direito em reset current branch to here and then carregar na opção hard!!

# Atenção, se eu fechar o aplictivo, todos os commits desaparecem!!!!

import datetime

todos: list = []


def show_information(lista: list) -> None:
    for indice, item in enumerate(lista):
        print(f'{indice + 1}: {item}')


def main():
    while True:
        now = datetime.datetime.now().strftime('%d %b %Y, %H:%M:%S')
        print(now)

        user_action: str = input('Type add, show, edit, remove or exit: ').strip().casefold()

        if user_action.startswith('add'):
            try:
                if user_action.split()[1] != '':
                    todos.append(' '.join(user_action.split()[1:]))
            except IndexError:
                todo: str = input('Enter a todo: ').title().strip()
                todos.append(todo)

        elif user_action == 'show':
            show_information(todos)

        elif user_action.startswith('edit'):
            show_information(todos)
            try:
                user_choice: int = int(''.join(user_action.split()[1:]))
            except ValueError:
                user_choice: bool = False
            number: int = user_choice or int(input('Number of the todo to edit: '))
            new_todo: str = input('Enter new todo: ').strip().title()
            try:
                todos[number - 1] = new_todo
            except IndexError:
                print('Não existe esse todo')

        elif user_action.startswith('remove'):
            try:
                user_choice: int = int(''.join(user_action.split()[1:]))
            except ValueError:
                user_choice: bool = False
            number: int = user_choice or int(input('Number of the todo to remove: '))
            del todos[number - 1]

        elif user_action == 'exit':
            break


if __name__ == '__main__':
    main()

    with open('Files/todo.txt', 'w', encoding='utf-8') as input_file:
        for index, element in enumerate(todos):
            print(f'{index + 1}: {element}', file=input_file)

    print('Bye!')
