#1. Usando input() con split()
input_string = input("Enter numbers: ")  # "12 9 61 5 14"
numbers = list(map(int, input_string.split()))  # Convierte cada número en entero
print(numbers)

#2. Usando map() directamente con input()
numbers = list(map(int, input().split()))
print(numbers)


#3. Usando list comprehension
numbers = [int(x) for x in input().split()]
print(numbers)


#4. Leer directamente como una cadena y procesarla
numbers = [int(num) for num in input("Enter numbers: ").strip().split()]
print(numbers)

#5. Usando sys.stdin.read para múltiples líneas
#import sys
# numbers = list(map(int, sys.stdin.read().split()))
print(numbers)
