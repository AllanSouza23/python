'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''
km = float(input('Qual a distância do percurso em Km? '))
if km <= 200:
    valor = 0.5 * km
else:
    valor = 0.45 * km
print(f'O valor de sua passagem é de R$ {valor:.2f}')
