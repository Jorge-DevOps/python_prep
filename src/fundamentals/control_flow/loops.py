if __name__ == "__main__":
# LOOPS 
#1. Bucle for (para iterar sobre secuencias como listas, tuplas, cadenas, etc.)
    # Ejemplo con lista
    for i in [1,2,3,4,5,6]:
        break
    # Ejemplo con rango de números
    for i in range(5):
        break
#2. Bucle while (ejecuta el código mientras se cumpla una condición)
    # Ejemplo básico de while
    i = 0
    while i < 5:
        # print(i)
        i += 1 

#3. for con enumerate() (obtiene tanto el índice como el valor de la secuencia)
    # Ejemplo con enumerate
    my_list = ['a','b','c','d']
    for index, value in enumerate(my_list):
        break
        # print(f'index: {index} value: {value}')


#4. for con zip() (iterar sobre dos o más secuencias simultáneamente)
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    for num,letter in zip(list1,list2):
        # print(f'{num} -> {letter}')
        break

#5. for con range() (iterar sobre una secuencia de números con un inicio, final y paso especificados)
    # Ejemplo con range
    for i in range(2, 10, 2):  # Empieza en 2, termina antes de 10, paso de 2
        # print(i)
        break



#6. Comprehensions (listas, diccionarios, conjuntos)
    # Ejemplo de list comprehension
    squares = [x**2 for x in range(5)]
    # print(squares)  # [0, 1, 4, 9, 16]

    # Ejemplo de set comprehension
    squares_set = {x**2 for x in range(5)}
    # print(squares_set)  # {0, 1, 4, 9, 16}

    # Ejemplo de dict comprehension
    squares_dict = {x: x**2 for x in range(5)}
    # print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#7. for con continue (salta a la siguiente iteración)
# Ejemplo con continue
    for i in range(5):
        if i == 3:
            continue  # Salta cuando i es 3
        print(i)

#8. for con break (detiene el loop)
    # Ejemplo con break
    for i in range(5):
        if i == 3:
            break  # Detiene el bucle cuando i es 3
        # print(i)

#9. for con else (ejecuta código al final del loop si no se usa break)
    # Ejemplo con else
    for i in range(5):
        print(i)
    else:
        print("Bucle terminado sin break")


#10. for con pass (no hace nada, útil como placeholder)
    # Ejemplo con pass
    for i in range(5):
        if i == 2:
            pass  # No hace nada, simplemente pasa al siguiente
        print(i)

#11 The for _ in loop is a variation of the for loop in Python, where the underscore (_) is used as a placeholder when the loop variable is not needed.
    for _ in range(5):
        print("Hello")
