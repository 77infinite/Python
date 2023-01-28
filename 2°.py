import math

A = float(input("Digite o valor do A da expressão: "))
B = float(input("Digite o valor do B da expressão: "))
C = float(input("Digite o valor de C da expressão: "))

delta = B**B -4*A*C
if delta < 0:
    print("Não existe raizes!!")
else:
    Raiz = math.sqrt(delta)
    X1 = (-B + Raiz) / (2*A)
    X2 = (-B - Raiz) / (2*A)