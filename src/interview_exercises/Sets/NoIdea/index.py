if __name__ == "__main__":
    size_1 = input()
    set_1 = set(map(int, input().split()))
    set_like = set(map(int, input().split()))
    set_unlike = set(map(int, input().split()))

    ######## Different way same result
    # countLike = sum(1 for x in set_1 if x in set_like)
    # countUnLike = sum(1 for x in set_1 if x in set_unlike)
    ######## Different way same result
    # countLike = len(set_1 & set_like)
    # countUnLike = len(set_1 & set_unlike)
    
    ######## Different way same result
    happiness = 0
    for i in set_1:
        if(i in set_like):
            happiness += 1
        elif(i in set_unlike):
            happiness -= 1

    print(happiness)