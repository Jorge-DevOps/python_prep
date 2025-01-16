if __name__ == "__main__":
    main_set = list(map(int(),input().split()))
    sizeSets = int(input())
    is_strict_superset = True

    for _ in range(sizeSets):
        other_set = list(map(int(),input().split()))

        if not (main_set > other_set):
            is_strict_superset = False
            break
print(is_strict_superset)
        