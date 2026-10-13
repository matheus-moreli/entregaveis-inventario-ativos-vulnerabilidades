from statistics import mean, median, multimode, pstdev


# Resultado de risco.calcular_riscos sobre dados/inventario.json do projeto
# principal em 13/10/2026, na ordem dos IDs 1 a 6 (amostra fictícia).
riscos = [9.8, 10.0, 9.8, 12.8, 0.0, 7.8]
print("Ativos na amostra:", len(riscos))
print("Média:", mean(riscos))
print("Mediana:", median(riscos))
print("Moda:", multimode(riscos))
print("Desvio padrão populacional:", pstdev(riscos))
print("Amostra didática: não representa o parque real nem mede energia.")
