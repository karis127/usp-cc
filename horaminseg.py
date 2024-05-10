numero = int(input("Digite a quantidade de segundos para converter em horas, minutos e segundos: "))

horas = numero // 3600
minutos = (numero % 3600) // 60
segundos = numero % 60

print("Isto equivale a {} horas, {} minutos e {} segundos". format(horas, minutos, segundos))
