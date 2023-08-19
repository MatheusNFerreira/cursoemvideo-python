import math

def calcular_raizes(a, b, c):
    discriminante = b ** 2 - 4 * a * c

    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return raiz1, raiz2
    elif discriminante == 0:
        raiz = -b / (2 * a)
        return raiz, raiz
    else:
        return None  # Não existem raízes reais


# Solicitar os coeficientes ao usuário
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Calcular e exibir as raízes
raizes = calcular_raizes(a, b, c)
if raizes:
    raiz1, raiz2 = raizes
    print(f"Raiz 1: {raiz1}")
    print(f"Raiz 2: {raiz2}")
else:
    print("Não existem raízes reais.")