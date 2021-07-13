'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'''
nome = str(input('Digite o seu nome completo: ')).strip()
separa = nome.split()
print('Seu primeiro nome é: {}'.format(separa[0]))
print('Seu último nome é: {}'.format(separa[-1]))
