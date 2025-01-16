if __name__ == "__main__":
    size = input()
    set_1 = set(map(int, input().split()))
    size2 = input()
    set_2 = set(map(int, input().split()))
    ## va a imprimir el numero de elementos que estan solo en el set 1 eliminando los que estan en ambos set
    print(len(set_1.difference(set_2)))
