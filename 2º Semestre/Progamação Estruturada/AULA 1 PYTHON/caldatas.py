from datetime import datetime

def calcular_diferenca(datastr1, datastr2):
    # Converter strings para objetos datetime (aceitando formato DD/MM/YYYY)
    data1 = datetime.strptime(datastr1, "%d/%m/%Y")
    data2 = datetime.strptime(datastr2, "%d/%m/%Y")
    
    # Garantir que data1 seja a menor
    if data1 > data2:
        data1, data2 = data2, data1
    
    # Calcular diferença total em dias
    diferenca_dias = (data2 - data1).days
    
    # Converter para anos, meses e dias aproximados
    anos = diferenca_dias // 365
    meses = (diferenca_dias % 365) // 30
    dias = (diferenca_dias % 365) % 30
    
    return anos, meses, dias

# Entrada do usuário
data_inicial = input("Digite a data inicial (DD/MM/YYYY): ")
data_final = input("Digite a data final (DD/MM/YYYY): ")

# Calcular diferença
anos, meses, dias = calcular_diferenca(data_inicial, data_final)
print(f"Diferença: {anos} anos, {meses} meses e {dias} dias")

