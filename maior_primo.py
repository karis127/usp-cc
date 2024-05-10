def ehPrimo(numero):

    contador = 2
    eh_primo = True

    if numero == 0:
        return False

    else:
        while contador < numero:
            if numero % contador == 0:
                eh_primo = False
            contador += 1


        return eh_primo
   

def maior_primo(numero):

    while not ehPrimo(numero):
        numero -= 1
    return numero

def maior_primo_dowsley(numero):
    while numero >= 0:
        if ehPrimo(numero):
            return numero
        numero -= 1
