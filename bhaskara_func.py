import math

def main():
    a = float(input("Digite o a: "))
    b = float(input("Digite o b: "))
    c = float(input("Digite o c: "))
    imprime_raizes(a, b, c)

def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d == 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        print("a raiz única desta equação é {}".format(x1))

    else:    
        if d < 0:
            print("esta equação não possui raízes reais")

        else:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            print("as raízes da equação são {} e {}".format(x1, x2))
    
def delta(a, b, c):
    return b ** 2 -4 * a * c


    
