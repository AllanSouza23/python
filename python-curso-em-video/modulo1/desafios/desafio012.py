#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preco = float(input('Digite o valor total do produto: R$'))
desconto = (preco / 100) * 95
print(f'O preço do produto, com desconto de 5%, será R${desconto:.2f}')
