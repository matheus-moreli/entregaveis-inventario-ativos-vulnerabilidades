from itertools import product


def porta_and(a, b):
    return a and b


def porta_or(a, b):
    return a or b


def porta_not(a):
    return not a


print("A     B     AND     OR     NOT A")
for a, b in product([False, True], repeat=2):
    print(a, b, porta_and(a, b), porta_or(a, b), porta_not(a))

print("Von Neumann: CPU processa instruções; memória armazena dados; barramentos conectam componentes.")
