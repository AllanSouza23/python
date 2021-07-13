'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''
salario = float(input('Informe o valor do salário para saber qunato ganhará de aumento: '))
if salario > 1250.00:
    aumento = 0.1 * salario
    aum = '10%'
else:
    aumento = 0.15 * salario
    aum = '15%'
novo_sal = aumento + salario
print(f'A partir do salário de R$ {salario:.2f}: \nVocê recebeu um aumento de {aum}, totalizando R$ {aumento:.2f} e com isto seu novo salário é R$ {novo_sal:.2f}')