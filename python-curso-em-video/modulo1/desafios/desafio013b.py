#Crie um programa que leia o valor de um produto com as seguintes condições
#Se pagar a vista ele tem um desconto de 10%
#Se pagar a prazo (parcelar) ele tem um aumento de 8%
produto = float(input('Digite o valor do produto: R$'))
desconto = (produto / 100) * 90
parcela = (produto / 100) * 108
print(f'A partir do produto de R${produto:.2f}:')
print(f'Se for comprado a vista, com desconto de 10%, seu valor será R${desconto:.2f}')
print(f'Se a compra for parcelada, com aumento de 8%, seu valor será R${parcela:.2f}')
