import math

A = float(input('Digite o valor do A da expressão: '))
B = float(input('Digite o valor do B da expressão: '))
C = float(input('Digite o valor do C da expressão: '))
Delta = (B^2) + (-4.0 * A * C)
print("Valor de Delta: ", Delta)

if Delta < 0:
    print("Não possui raizes")
elif(Delta > 0):
    Raiz = math.sqrt(Delta)
    X1 = (-B + Raiz)/(2*A)
    X2 = (-B - Raiz)/(2*A)
    print('As raizes desta equação são: ', X1, X2)
    
elif (Delta == 0):
    print("Somente uma raiz")
    Raiz = math.sqrt(Delta)
    X1 = (-B + Raiz)/(2*A)
    X2 = (-B - Raiz)/(2*A)
    print('A raiz desta equação é: ', X1)

Xv = -B/ (2*A)
Yv = -Delta/ (4/A)
print ("Os valores dos vertices são: ", Xv, Yv)
