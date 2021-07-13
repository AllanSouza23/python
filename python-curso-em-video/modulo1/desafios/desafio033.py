''' Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
n1 = int(input('Digite o primeiro número: '))
menor = n1
maior = n1
n2 = int(input('Digite o segundo número: '))
if n2 < menor:
    menor = n2
else: 
    maior = n2
n3 = int(input('Digite o terceiro número: '))
if n3 < menor:
    menor = n3
else:
    maior = n3
print('O maior número é {} e o menor é {}'.format(maior, menor))