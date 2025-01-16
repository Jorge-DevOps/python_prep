if __name__ == "__main__":
    n = int(input())
    x = list(map(int, input().split()))
    unique_rooms = set(x)
    ### Formula para determinar el numero exacto que se repite N veces (compleja)
    print((sum(unique_rooms) * n - sum(x)) // (n - 1))
    