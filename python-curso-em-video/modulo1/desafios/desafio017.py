#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa
from math import hypot
co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
print(f'Com {co:.2f} de comprimento no cateto oposto e {ca:.2f} de comprimento no cateto adjacente, o comprimento da hipotenusa é {hypot(co, ca):.2f}.')
