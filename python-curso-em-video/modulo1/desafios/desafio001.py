#DESAFIO 001
#Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado.
import ansicon
ansicon.load()
nome = input('Qual é o seu nome? ')
print(f'Olá \033[2;33m{nome:}\033[m! Prazer em te conhecer!')
ansicon.unload()
