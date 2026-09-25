# A função recebe dados como parâmetros e evita repetir o mesmo print.

def mostrar_ativo(nome_ativo, responsavel):
    print(f"Ativo: {nome_ativo} | Responsável: {responsavel}")


nome = input("Nome do ativo: ")
responsavel = input("Responsável: ")
mostrar_ativo(nome, responsavel)
