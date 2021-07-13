numero = int(input("Digite um número inteiro (0 para sair): "))
lista = []
while numero != 0:
    lista.append(numero)
    numero = int(input("Digite um número inteiro (0 para sair): "))
lista.sort()
print(lista)