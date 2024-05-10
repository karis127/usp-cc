import math

a = float(input("Digite o a: "))
b = float(input("Digite o b: "))
c = float(input("Digite o c: "))

delta = b ** 2 -4 * a * c

if delta == 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    if x1 == x2:
        print("a raiz dupla desta equação é {}".format(x1))
    else:
        print("a raiz única desta equação é {}".format(x1))

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    #print("as raízes da equação são {} e {}".format(x1, x2))

    if x1 < x2:
        print("as raízes da equação são {} e {}".format(x1, x2))
    if x1 > x2:
        print("as raízes da equação são {} e {}".format(x2, x1))

else:
    print("esta equação não possui raízes reais")
