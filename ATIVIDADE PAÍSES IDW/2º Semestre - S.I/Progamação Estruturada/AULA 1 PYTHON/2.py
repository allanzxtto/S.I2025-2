gen= (input("Digite seu gênero: ")).strip().lower()
idade= int(input("Digite sua idade: "))

if gen == "feminino" and idade >= 18:
   print("Bem vindo ao clube da Luluzinha")
else:
   print("Você não pode entrar criança")