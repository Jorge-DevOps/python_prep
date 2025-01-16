if __name__ == "__main__":
    size = input()
    set_1 = set(map(int, input().split()))
    size2 = input()
    set_2 = set(map(int, input().split()))
    ### numeros que estan en uno o en el otro pero no en los dos
    print(len(set_1.symmetric_difference(set_2)))