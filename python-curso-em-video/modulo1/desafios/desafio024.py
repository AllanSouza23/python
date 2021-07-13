'''Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.'''
cidade = str(input('Digite o nome da cidade: ')).strip()
separa = cidade.split()
if separa[0].capitalize() == 'Santo':
    print(f'A cidade {cidade} começa com Santo')
else:
    print(f'A cidade {cidade} não começa com Santo')
