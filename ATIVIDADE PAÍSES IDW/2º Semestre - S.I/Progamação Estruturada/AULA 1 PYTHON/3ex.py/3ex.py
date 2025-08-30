gain= float(input("Digite o seu salário: "))
desconto1= 0.1
desconto2= 0.15

if gain <= 500:
    multiplicacao= gain*desconto1
    gaintotal= gain - desconto1
    print("O seu salário é R$: ", gaintotal)
else:
    multiplicacao= gain*desconto2
    gaintotal= gain - desconto2
    print("O seu salário é R$: ", gaintotal)
