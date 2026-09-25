# Tupla não muda depois de criada; set não repete valores.

tipos_de_ativo = ("Notebook", "Servidor", "Roteador", "Aplicação web")
vulnerabilidades_ativo_a = {"Senha fraca", "Software desatualizado"}
vulnerabilidades_ativo_b = {"Software desatualizado", "Porta exposta"}

print("Tipos disponíveis:", tipos_de_ativo)
print("Sem repetição:", vulnerabilidades_ativo_a)
print("Em ambos os ativos:", vulnerabilidades_ativo_a.intersection(vulnerabilidades_ativo_b))
print("Em pelo menos um ativo:", vulnerabilidades_ativo_a.union(vulnerabilidades_ativo_b))
print("Somente no ativo A:", vulnerabilidades_ativo_a.difference(vulnerabilidades_ativo_b))
