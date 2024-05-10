n = int(input("digite a sequencia de numeros: "))

lastDigit = 0
prevLastDigit = 1

while lastDigit != prevLastDigit:
    lastDigit = n % 10
    novoN = n // 10
    prevLastDigit = novoN % 10
    n = n // 10

if lastDigit == 0 and prevLastDigit == 0:
    print("não")
else:
    print("sim")
