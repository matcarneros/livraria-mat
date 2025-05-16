# Mensagem
print("----------------------------------------------------------")
print("------------Bem-vindo a livraria do Matheus!--------------")
print("----------------------------------------------------------")
print("------------Desenvolvido por Matheus Santos---------------")

# Lista de livros e id_global
lista_livro = []
id_global = 0

# Cadastro do livro


def cadastrar_livro(id):
    nome = input("Informe o nome do livro: ")
    autor = input("Informe o autor do livro: ")
    editora = input("Informe a editora do livro: ")

    livro = {"id": id, "nome": nome, "autor": autor, "editora": editora}
    lista_livro.append(livro)

# Consultar o livro


def consultar_livro():
    while True:
        print("\nOpções de consulta:")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Autor")
        print("4. Retornar ao menu")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nTodos os livros cadastrados:")
            for livro in lista_livro:
                print(
                    f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")

        elif opcao == "2":
            id_busca = int(input("Informe o ID do livro: "))
            encontrado = False
            for livro in lista_livro:
                if livro['id'] == id_busca:
                    print(
                        f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
                    encontrado = True
            if not encontrado:
                print("Livro não encontrado pelo ID informado.")

        elif opcao == "3":
            autor_busca = input("Informe o autor do livro: ")
            encontrados = [
                livro for livro in lista_livro if livro['autor'].lower() == autor_busca.lower()]
            if encontrados:
                for livro in encontrados:
                    print(
                        f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
            else:
                print("Nenhum livro encontrado para o autor informado.")

        elif opcao == "4":
            break

        else:
            print("Opção inválida. Tente novamente.")

# Remover livro


def remover_livro():
    while True:
        id_remover = int(input("Informe o ID do livro a ser removido: "))
        encontrado = False
        for livro in lista_livro:
            if livro['id'] == id_remover:
                lista_livro.remove(livro)
                print(f"Livro com ID {id_remover} removido com sucesso.")
                encontrado = True
                break
        if not encontrado:
            print("ID inválido. Tente novamente.")
        else:
            break


# Menu principal

while True:
    print("\nMenu Principal:")
    print("1. Cadastrar Livro")
    print("2. Consultar Livro")
    print("3. Remover Livro")
    print("4. Encerrar Programa")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        id_global += 1
        cadastrar_livro(id_global)

    elif opcao == "2":
        consultar_livro()

    elif opcao == "3":
        remover_livro()

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")



