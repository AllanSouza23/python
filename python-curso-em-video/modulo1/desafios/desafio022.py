'''Crie um programa que leia o nome completo de uma pessoa e mostre:
o nome com todas as letras maiusculas
o nome com todas as letras minusculas
quantas letras tem o nome sem contar os espaços
quantas letras tem o primeiro nome'''
nome = str(input('Digite seu nome: ')).strip()
print(f'Seu nome em letras maiúsculas é: {nome.upper()}')
print(f'Seu nome em letras minúsculas é: {nome.lower()}')
print('Seu nome possui {} letras'.format(len(nome) - nome.count(' ')))
separado = nome.split()
print(f'Seu primeiro nome é {separado[0]} e ele possui {len(separado[0])} letras')