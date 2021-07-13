def soma_elementos(lista):
    soma =0
    for elemento in lista:
        soma += elemento
    return soma
lista = input()
lista_aux = []
lista = lista.split(',')
for e in lista:
    lista_aux.append(int(e))
soma_elementos(lista_aux)