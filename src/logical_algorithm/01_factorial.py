def get_factorial(n):
    result = 1
    if n > 1: 
        for i in range(1,n+1):
            result = result * i 
        return result
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(get_factorial(n))


## Second improved version
def get_factorial_2(n):
    if n < 0:
        raise ValueError("Factorial es not defined for negative numbers")
    result_2 = 1
    for i in range(1, n+1):
        result_2 *= i

if __name__ == "__main__":
    try:
        n = int(input("Enter a number: "))
        print(get_factorial(n))
    except ValueError as e:
        print(e)
