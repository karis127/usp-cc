n = int(input("digite a sequencia de numeros: "))
soma = 0
final = 0

while n != 0:
    final = n % 10
    n = n // 10
    soma = soma + final

print(soma)


