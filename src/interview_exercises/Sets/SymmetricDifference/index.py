if __name__ == "__main__":
    size_1 = int(input())
    set_1 = set(map(int, input().split()))
    size_2 = int(input())
    set_2 =  set(map(int, input().split()))
    # result_set = (set_1.difference(set_2)).union((set_2.difference(set_1)))
    ### numeros que estan en uno o en el otro pero no en los dos
    result_set = sorted(set_1.symmetric_difference(set_2))
    for x in result_set:
        print(x)
    