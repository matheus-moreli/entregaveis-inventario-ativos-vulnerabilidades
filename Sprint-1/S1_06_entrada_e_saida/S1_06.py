# input recebe um texto digitado. print mostra uma saída para quem usa o programa.

identificador = input("ID do ativo: ")
nome = input("Nome ou hostname: ")
responsavel = input("Responsável: ")
localizacao = input("Setor ou localização: ")

# Uma f-string junta texto e variáveis em uma saída organizada.
print(f"\nAtivo {identificador}: {nome}\nResponsável: {responsavel}\nLocalização: {localizacao}")
