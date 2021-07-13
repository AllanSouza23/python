n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2 
di = n1 // n2
e = n1 **n2
print('Entre os termos {} e {} nós temos que:'.format(n1, n2))
print('A soma vale {}\nO produto vale {}\nA divisão vale {:.2f}'.format(s, m, d))
print('A divisão inteira vale {}\nA potência vale {}'.format(di, e))
