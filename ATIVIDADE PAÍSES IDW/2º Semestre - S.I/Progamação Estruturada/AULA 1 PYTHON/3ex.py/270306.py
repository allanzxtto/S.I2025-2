idade=int(input("Digite sua idade: "))
genero= input("Digite o gênero de filme (ação, comédia, drama): ").strip().lower()

if idade>=16 and genero=="ação":
    print("Você pode assistir ação")
elif idade>=10 and idade>=18 and genero=="comédia":
    print("Você pode assistir comédia")
elif idade>=18:
    print("Você pode assistir todos os gêneros!")
else:
    print("Você pode assitir drama")
