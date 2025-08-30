cont = 0
tabuada = 0
num = int(input("Entre com um número:"))

while cont <= 10:
    tabuada = num * cont
    
    print( num, "x", cont, "=", tabuada)
    cont += 1