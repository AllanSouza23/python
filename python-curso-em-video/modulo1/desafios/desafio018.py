#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import sin, cos, tan, radians
angulo = int(input('Digite um ângulo qualquer: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'A partir do ângulo {angulo:}°, nós temos que:')
print(f'Seu seno é {seno:.2f}')
print(f'Seu cosseno é {cosseno:.2f}')
print(f'Sua tangente é {tangente:.2f}')
