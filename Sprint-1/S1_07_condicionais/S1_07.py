# if, elif e else permitem escolher uma mensagem conforme a nota informada.

nota_cvss = float(input("Nota CVSS da vulnerabilidade (0 a 10): "))

if nota_cvss >= 9:
    severidade = "Crítica"
elif nota_cvss >= 7:
    severidade = "Alta"
elif nota_cvss >= 4:
    severidade = "Média"
else:
    severidade = "Baixa"

print(f"Severidade classificada: {severidade}")
