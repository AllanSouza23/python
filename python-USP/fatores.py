numero = int(input("Digite um número inteiro maior que 1: "))
fator = 2
multiplicidade = 0

while numero > 1:
    while numero % fator == 0:
        multiplicidade += 1
        numero = numero / fator
    if multiplicidade > 0:    
        print(f"fator {fator} multiplicidade = {multiplicidade}")
    fator += 1
    multiplicidade = 0