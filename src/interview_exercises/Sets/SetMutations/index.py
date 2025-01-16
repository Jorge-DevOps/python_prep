if __name__ == "__main__":

    a=int(input())
    n=set(map(int,input().split()))
    N=int(input())

    #### operaciones con el tipo de dato set update, intersection, difference
    for i in range(N):
        c=input().split()
        d=set(map(int,input().split()))
        if(c[0]=='update'):
            n.update(d)
        elif(c[0]=='intersection_update'):
            n.intersection_update(d)
        elif(c[0]=='difference_update'):
            n.difference_update(d)
        else:
            n.symmetric_difference_update(d)
            
    print(sum(n))