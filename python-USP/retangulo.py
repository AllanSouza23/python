def imprimeForma(x, y):
    while y > 0:
        print(x * "#")
        y -= 1

largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

imprimeForma(largura, altura)