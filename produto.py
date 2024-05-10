tamanho = int(input("Digite o tamanho da sequencia de numeros: "))
produto = 1     #multiplicador
i = 0           #contador

while i < tamanho:
    valor = float(input("Digite um valor a ser multiplicado: "))
    produto = produto * valor
    i = i + 1

print(produto)
    
