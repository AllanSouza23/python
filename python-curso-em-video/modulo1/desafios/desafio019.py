#Um professor que sortear um de seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
from random import choice 
a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ') 
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do quarto aluno: ')
lista = [a, b, c, d]
sorteado = choice(lista)
print(f'O(A) aluno(a) escolhido(a) foi o(a): {sorteado:}')
