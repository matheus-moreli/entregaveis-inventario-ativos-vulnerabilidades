# O dicionário relaciona o ID da vulnerabilidade aos seus dados.

vulnerabilidades = {}
codigo = input("Código da vulnerabilidade: ")
vulnerabilidades[codigo] = {
    "descricao": input("Descrição: "),
    "severidade": input("Severidade: "),
    "status": input("Status inicial: "),
}

novo_status = input("Novo status (vazio para manter): ")
if novo_status:
    vulnerabilidades[codigo]["status"] = novo_status

print("\nVulnerabilidade atualizada:")
print(vulnerabilidades[codigo])
