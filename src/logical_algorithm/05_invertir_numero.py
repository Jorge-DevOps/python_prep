def invertir_numero(n):
    nstr = str(n)
    result = ""
    for i in range(len(nstr)):
        result += nstr[len(nstr) - i - 1]
    return result


if __name__ == "__main__":
    n = int(input("Digite un numero: "))
    print(invertir_numero(n))
