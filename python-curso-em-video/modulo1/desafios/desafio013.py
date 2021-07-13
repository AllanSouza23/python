#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
salario = float(input('Digite o seu salário: R$'))
aumento = (salario / 100) * 115
print('Parabéns, você teve um aumento salarial de 15%!')
print(f'O seu salrio antigo era de R${salario:.2f}')
print(f'Seu novo salário é de R${aumento:.2f}')
