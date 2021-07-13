#Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
altura = float(input('Por favor, digite a altura da parede: '))
largura = float(input('Por favor, digite a largura da parede: '))
area = altura * largura
tinta = area / 2
print(f'Tendo a parede {altura:}m X {largura:}m:')
print(f'A área da parede é {area:.2f}m² e serão necessários {tinta:.2f}l de tinta para pintá-la.')
