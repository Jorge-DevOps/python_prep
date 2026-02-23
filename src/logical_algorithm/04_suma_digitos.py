def calcular_suma_digitos(n):
    numb = str(n)
    result = 0
    for i in range(0, len(numb)):
        result += int(numb[i])
    return result


if __name__ == "__main__":
    n = int(input("Ingrese un numero: "))
    print(calcular_suma_digitos(n))
