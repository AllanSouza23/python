#DESAFIO 004
#Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as possíveis informações sobre ele.

a = input('Digite algo: ')

print(f'Só tem espaços? {a.isspace():}')
print(f'É um número? {a.isnumeric():}')
print(f'É alfabético? {a.isalpha():}')
print(f'É alfanumérico? {a.isalnum():}')
print(f'Está em maiúsculas? {a.isupper():}')
print(f'Está em minúsculas? {a.islower():}')
print(f'Está capitalizada? {a.istitle():}')