total_dias=int(input("Quantos dias você ficou hospedado: "))
valor_diaria=float(input("O valor da sua diária é R$: "))
total_consumo=float(input("O total consumido em R$: "))

total_a_pagar=total_dias*valor_diaria+total_consumo

print("Seu gasto no hotel foi de", total_a_pagar,"reais")