'''Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.'''
nome = str(input('Digite seu nome completo: ')).strip()
if ('silva' in nome.lower()) == True:
    print(f'O nome {nome} possui Silva')
else:
    print(f'O nome {nome} não possui Silva')
