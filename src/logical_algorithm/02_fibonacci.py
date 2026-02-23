def get_fibonacci_series(n):

    if n > 0:
        a = 0
        b = 1
        for i in range (0,n):
            c = a + b
            a = b
            b = c
            print(c, end=" ")


if __name__ == "__main__":
    try:
        n = int(input("Enter a number: "))
        get_fibonacci_series(n)
    except ValueError as e:
        print(e)

# I= 0
# 1) 1 + 1 = 2
# 2) 1 + 2 = 3
# 3) 2 + 3 = 5
# 4) 3 + 5 = 8
# 5) 5 + 8 = 13
