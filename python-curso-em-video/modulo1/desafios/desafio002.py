#DESAFIO 002
#Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.
import ansicon
ansicon.load()

nome = input('Qual o seu nome? ')
dia = input('Em que dia você nasceu? ')
mes = input('Em que mês você nasceu? ')
ano = input('Em que ano você nasceu? ')

print(f'Você nasceu no dia \033[2;33m{dia:}\033[m de \033[2;33m{mes:}\033[m de \033[2;33m{ano:}\033[m. Correto \033[2;34m{nome:}\033[m?')

ansicon.unload()