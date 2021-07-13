def imprimeForma(x, y):
    print(x * "#")
    y -= 1
    while y > 1:
        print("#" + (x - 2) * " " + "#")
        y -= 1
    print(x * "#")


largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

imprimeForma(largura, altura)