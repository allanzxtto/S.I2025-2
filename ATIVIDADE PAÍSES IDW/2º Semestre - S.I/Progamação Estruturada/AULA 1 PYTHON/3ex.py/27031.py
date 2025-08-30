rifa= int(input("Quantos números você quer da nossa rifa por apenas R$3,66: "))
televisão= float(input("Qual o valor da televisão que você quer ganhar?: "))
valor=3.66

vendidos= rifa*valor
liquido= vendidos-televisão

print("O lucro líquido da rifa é de R$", liquido)