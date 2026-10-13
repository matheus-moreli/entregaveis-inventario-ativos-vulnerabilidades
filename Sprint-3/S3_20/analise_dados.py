from statistics import mean, median, multimode, pstdev


riscos = [9.8, 10.0, 9.8, 12.8, 0.0, 7.8]
print("Média:", mean(riscos))
print("Mediana:", median(riscos))
print("Moda:", multimode(riscos))
print("Desvio padrão populacional:", pstdev(riscos))
print("LGPD: o sistema deve coletar apenas dados necessários e restringir acesso por função.")
print("Sustentabilidade: manter inventário evita troca desnecessária de ativos e orienta manutenção.")
