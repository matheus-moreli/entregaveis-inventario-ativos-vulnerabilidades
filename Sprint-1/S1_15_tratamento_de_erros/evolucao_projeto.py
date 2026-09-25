import json

# Complemento da evolução do inventário; não substitui o exercício S1_15.py.
ARQUIVO = "inventario_exemplo.json"

try:
    id_ativo = int(input("ID do novo ativo: "))
    nome_ativo = input("Nome do ativo: ").strip()

    if nome_ativo == "":
        raise ValueError("O nome do ativo não pode ficar vazio.")

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        ativos = json.load(arquivo)

    ativos[str(id_ativo)] = {"id": id_ativo, "nome": nome_ativo, "vulnerabilidades": []}

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(ativos, arquivo, ensure_ascii=False, indent=2)

    print("Ativo registrado e salvo com sucesso.")

except ValueError as erro:
    print(f"Entrada inválida: {erro}")
except FileNotFoundError:
    print("Execute a S1_14 ou crie o arquivo JSON antes deste complemento.")
except json.JSONDecodeError:
    print("O arquivo JSON não está em um formato válido.")
