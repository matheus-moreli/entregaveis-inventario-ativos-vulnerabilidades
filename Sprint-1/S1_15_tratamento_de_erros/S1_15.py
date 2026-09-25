import json


arquivo_json = "ativos.json"

try:
    identificador = int(input("ID numérico do ativo: "))
    if identificador <= 0:
        raise ValueError("O ID deve ser maior que zero.")

    ativo = {
        "id": identificador,
        "nome": input("Nome do ativo: "),
        "responsavel": input("Responsável: "),
    }

except ValueError as erro:
    print("Erro de entrada:", erro)

else:
    try:
        with open(arquivo_json, "w", encoding="utf-8") as arquivo:
            json.dump(ativo, arquivo, ensure_ascii=False, indent=2)
        print("Ativo gravado com sucesso.")
    except OSError:
        print("Erro ao gravar o arquivo de ativos.")

finally:
    print("Fim da tentativa de cadastro.")
