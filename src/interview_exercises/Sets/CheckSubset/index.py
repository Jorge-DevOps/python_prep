if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a = int(input())
        set_number = set(map(int,input().split()))
        b = int(input())
        set_number1 = set(map(int,input().split()))
        if(set_number < set_number1):
            print(True)
        else:
            print(False)
            
        