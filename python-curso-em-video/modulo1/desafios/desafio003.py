#DESAFIO 003
#Crie um script Python que leia dois números e tente mostrar a soma entre eles.
import ansicon
ansicon.load()
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
soma = n1 + n2

print(f'A soma entre \033[2;34m{n1:}\033[m e \033[2;35m{n2:}\033[m é igual a \033[2;32m{soma:}\033[m')
ansicon.unload()