import json


# JSON permite que o dicionário continue existindo depois que o programa fecha.
arquivo_json = "vulnerabilidades.json"
vulnerabilidades = {}

try:
    with open(arquivo_json, "r", encoding="utf-8") as arquivo:
        vulnerabilidades = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo ainda não existe. Uma nova base será criada.")
except json.JSONDecodeError:
    print("Arquivo JSON inválido. Os dados não foram carregados.")

codigo = input("Código da vulnerabilidade: ")
vulnerabilidades[codigo] = {
    "descricao": input("Descrição: "),
    "severidade": input("Severidade: "),
    "status": input("Status: "),
}

try:
    with open(arquivo_json, "w", encoding="utf-8") as arquivo:
        json.dump(vulnerabilidades, arquivo, ensure_ascii=False, indent=2)
    print("Vulnerabilidade salva no JSON.")
except OSError:
    print("Não foi possível gravar o arquivo.")
