from math import sqrt

def get_primo(n):
    esPrimo= True
    raiz = sqrt(n)
    for i in range(2, int(raiz)):
        if n % i == 0:
            esPrimo = False
    return esPrimo

if __name__ == "__main__":
    n = int(input("Ingrese un numero: "))
    print(get_primo(n))
