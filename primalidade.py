numero = int(input())

contador = 2
eh_primo = True

if numero == 0:
    print("não primo")

else:
    while contador < numero:
        if numero % contador == 0:
            eh_primo = False
        contador += 1

    if eh_primo:
        print("primo")
    else:
        print("não primo")
