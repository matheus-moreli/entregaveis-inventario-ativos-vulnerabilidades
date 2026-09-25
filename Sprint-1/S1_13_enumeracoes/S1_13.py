from enum import Enum


# Enum evita escrever estados diferentes para a mesma situação.
class StatusAtivo(Enum):
    ATIVO = "Ativo"
    EM_MANUTENCAO = "Em manutenção"
    INATIVO = "Inativo"


print("1 - Ativo\n2 - Em manutenção\n3 - Inativo")
opcao = input("Status do ativo: ")

if opcao == "1":
    status = StatusAtivo.ATIVO
elif opcao == "2":
    status = StatusAtivo.EM_MANUTENCAO
else:
    status = StatusAtivo.INATIVO

print("Status escolhido:", status.value)
