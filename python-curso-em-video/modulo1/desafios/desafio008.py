#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Digite um valor em metros para realizar a conversão: '))
dm = m * 10
cm = m * 100
mm = m * 1000
km = m / 1000
hm = m / 100
dam = m / 10
print(f'{m:} m correspondem a:')
print(f'{km:} km \n{hm:} hm \n{dam:} dam \n{dm:.0f} dm \n{cm:.0f} cm \n{mm:.0f} mm')
