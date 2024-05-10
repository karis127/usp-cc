n = int(input())

cont_impar = 0
novo_numero = 1

while cont_impar < n:
    if novo_numero % 2 != 0:
        print(novo_numero)
        cont_impar += 1
    novo_numero += 1
