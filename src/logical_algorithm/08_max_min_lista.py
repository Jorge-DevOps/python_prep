def max_min(lista):
    max = lista[0]
    min = lista[0]
    for i in range(1,len(lista)):
        if lista[i] > max:
            max = lista[i]
        if lista[i] < min:
            min = lista[i]
    return f"max = {max} - min = {min}"
if __name__ == "__main__":
    n = input("Ingrese los valores: ")
    lista = [int(x) for x in n.split()]
    print(max_min(lista))
