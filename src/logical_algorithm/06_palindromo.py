def palindromo(n):
    isPalindromo=True
    for i in range(0,len(n)):
        if n[i] == n[(len(n)-1) - i]:
            isPalindromo = True
        else: 
            return False
    return isPalindromo

if __name__ == "__main__":
    n = input("ingrese un numero: ")
    print(palindromo(n))
