valor_financiado= float(input("O valor do financiamento da Kombi é R$: "))
valor_parcela= float(input("O valor de cada parcela é R$: "))
qtd_pagas= int(input("Quantas parcelas você já pagou: "))

totalpago= valor_parcela*qtd_pagas
falta= valor_financiado-totalpago
faltaparcelas= valor_financiado/valor_parcela-qtd_pagas

print("O valor pago até o momento é R$: ",totalpago)
print("O valor que você deve é R$:", falta)
print("A quantidade de parcelas que falta é:",faltaparcelas)


