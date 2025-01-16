if __name__ == "__main__":
    size = input()
    set_1 = set(map(int, input().split()))
    size2 = input()
    set_2 = set(map(int, input().split()))
    print(len(set_1.intersection(set_2)))