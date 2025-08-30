salario=float(input("Qual o valor do seu salário: R$ "))
imp1= 0.10
imp2=0.20

if salario<=2000:
    print("Insento do Imposto")

elif salario<=5000:
    imposto=salario-(salario*imp1)
    print("Seu salário liquido é", imposto, "reais")

else:
    impost=salario-(salario*imp2)
    print("O valor do seu salário liquido é", impost, "reais")
