
A1 = float(input("Digite a nota da 1° prova: "))
A2 = float(input("Digite a nota da 2° prova: "))
A3 = float(input("Digite a nota da 3° prova: "))
MED = (A1+A2+A3)/3

print("Sua média é igual a: %.1f" %(MED))

if MED==6:
    print("Passou")

else:
        if A1<=A2 and A1<=A3:
            DN=A1
            P6= DN+A2+A3
            P6M= 18-P6
            PF= P6M+DN
            print("Não Passou")
            print("A sua pior nota foi: ", A1)
            print("Você precisa tirar: ", PF)
        elif A2<=A1 and A2<=A3:
            DN=A2
            P6= DN+A1+A3
            P6M= 18-P6
            PF= P6M+DN
            print("Não Passou")
            print('A sua pior nota foi: ', A2)
            print("Você precisa tirar: ", PF)
        elif A3<=A1 and A3<=A2:
            DN=A3
            P6= DN+A2+A1
            P6M= 18-P6
            PF= P6M+DN
            print("Não Passou")
            print("A sua pior nota foi: ", A3)
            print("Você precisa tirar: ", PF)

    