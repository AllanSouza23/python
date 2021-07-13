#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere -> US$ 1,00 = R$ 3,27 ==============>Considere a cotação do dia 20/06/2020  -> US$1,00 = R$5,31 - euro 1,00 = R$5,94
real = float(input('Quantos reais você possui na carteira? R$'))
dolar = real / 5.31
euro = real / 5.94
print(f'Com R${real:.2f} você poderá comprar US${dolar:.2f} dólares ou {euro:.2f} euros!')
