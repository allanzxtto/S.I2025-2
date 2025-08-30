resposta= input("Deseja digitar um nome? S - Sim, N - Não\n").upper()
cont=1

while resposta !='N' and cont <= 50:
    nome= input("Digite um nome: ")
    resposta= input("Deseja digitar outro nome? S-Sim, N - Não\n").upper()
    cont += 1 
    if cont == 50:
        print("Número máximo de alunos atingido.")

print("Programa encerrado")