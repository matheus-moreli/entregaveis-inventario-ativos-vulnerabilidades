# Complemento da evolução do inventário; não substitui o exercício S1_09.py.
def mostrar_menu():
    print("\n1 - Cadastrar ativo")
    print("2 - Listar ativos")
    print("0 - Encerrar")


def cadastrar_ativo():
    nome_ativo = input("Nome do ativo: ")
    print(f"{nome_ativo} foi recebido para cadastro.")


mostrar_menu()
opcao = input("Escolha uma opção: ")

if opcao == "1":
    cadastrar_ativo()
