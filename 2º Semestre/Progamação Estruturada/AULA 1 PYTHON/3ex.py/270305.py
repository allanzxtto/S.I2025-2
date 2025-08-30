idade=int(input("Digite sua idade: "))

if idade>=18 and idade<=70:
    print("Votação autorizada")

elif idade==16 or idade==17:
    print("Vote com a autorização dos seus pais")

else:
    print("Votação negada")