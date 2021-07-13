'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''
vel = float(input('Qual a velocidade do veículo? '))
if vel > 80:
    print('MULTADO! Você excedeu o limite de 80 Km/h')
    km = vel - 80
    multa = 7 * km
    print('O valor a ser pago é de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')
