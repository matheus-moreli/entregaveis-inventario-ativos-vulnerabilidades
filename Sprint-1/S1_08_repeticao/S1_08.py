# while mantém o menu aberto até a pessoa escolher Sair.

opcao = ""
while opcao != "3":
    print("\n1 - Cadastrar ativo")
    print("2 - Listar ativos")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Cadastro selecionado.")
    elif opcao == "2":
        print("Listagem selecionada.")
    elif opcao == "3":
        print("Programa encerrado.")
    else:
        print("Opção inválida.")
