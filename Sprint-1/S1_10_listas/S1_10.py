# Uma lista guarda vários nomes de ativos e pode ser alterada durante o programa.

ativos = []
opcao = ""

while opcao != "4":
    print("\n1 - Adicionar ativo\n2 - Remover ativo\n3 - Listar ativos\n4 - Sair")
    opcao = input("Opção: ")

    if opcao == "1":
        ativos.append(input("Nome do ativo: "))
    elif opcao == "2":
        nome = input("Nome que será removido: ")
        if nome in ativos:
            ativos.remove(nome)
            print("Ativo removido.")
        else:
            print("Ativo não encontrado.")
    elif opcao == "3":
        print("Ativos cadastrados:", ativos)
    elif opcao != "4":
        print("Opção inválida.")
