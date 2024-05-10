cartao = int(input("numero do cartao: "))

cartaolido = 1
cartaoencontrado = False

while cartaolido != 0 and not cartaoencontrado:
    cartaolido = int(input("digite o numeor do proximo cartao: "))
    if cartaolido == cartao:
        cartaoencontrado = True


if cartaoencontrado:
    print("eba")
else:
    print("depressao")
