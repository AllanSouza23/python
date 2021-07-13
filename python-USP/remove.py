def remove_repetidos(lista):
    lista_aux = []
    for elemento in lista:
        if elemento not in lista_aux:
            lista_aux.append(elemento)
    lista_aux.sort()
    return lista_aux
lista = input()
lista_aux = []
lista = lista.split(',')
for e in lista:
    lista_aux.append(int(e))
remove_repetidos(lista_aux)