exame= input("Digite o nome do seu exame: ")
result= float(input("Digite o valor do seu exame: "))
refmin= 70
refmax= 99

if result > refmax:
    print("O seu",exame, "está acima do normal")

elif result < refmin:
    print("O seu", exame, "está abaixo do normal")

else:
    print("O seu exame está normal!!")