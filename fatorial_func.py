def fatorial(n):
    fat = 1
    while (n > fat):
        fat *= n
        n -= 1
    return fat

def numero_binomial(n, k):
    return fatorial(n) / (fatorial(k) * fatorial(n - k))
