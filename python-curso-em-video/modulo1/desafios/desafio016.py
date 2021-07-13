#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção Inteira.
#ex: Digite um número: 6.127
#O número 6.127 tem a parte Inteira 6.
from math import trunc
num = float(input('Digite um número: '))
print(f'O número {num:} tem a parte Inteira {trunc(num):}.')

