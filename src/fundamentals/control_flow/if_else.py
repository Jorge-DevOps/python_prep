if __name__ == "__main__":

    #if: Condición simple.
    x = 5
    if x > 3:
        print("x es mayor que 3")


#if-else: Alternativa entre dos caminos.

    x = 2
    if x > 3:
        print("x es mayor que 3")
    else:
        print("x no es mayor que 3")

#if-elif-else: Evaluación de múltiples condiciones.

    x = 10
    if x > 15:
        print("x es mayor que 15")
    elif x > 5:
        print("x es mayor que 5 pero menor o igual a 15")
    else:
        print("x es 5 o menor")


#Operadores lógicos (and, or, not): Para combinar o negar condiciones.
    x = 5
    y = 10
    if x > 3 and y < 15:
        print("x es mayor que 3 y y es menor que 15")
    if x > 3 or y < 15:
        print("Al menos una condición es verdadera")
    if not x < 3:
        print("x no es menor que 3")


#Expresiones condicionales: En una sola línea para mayor concisión.
    x = 7
    print("x es mayor que 5") if x > 5 else print("x es menor o igual a 5")

    x = 3
    result = "Mayor que 2" if x > 2 else "Menor o igual a 2"
    print(result)

#Anidación de if: Condiciones dentro de otras.
    x = 7
    y = 5
    if x > 5:
        if y < 10:
            print("x es mayor que 5 y y es menor que 10")
        else:
            print("x es mayor que 5 y y es mayor o igual a 10")
    else:
        print("x es menor o igual a 5")

#match (Python 3.10+): Un enfoque más estructurado similar a switch.
    x = 2
    match x:
        case 1:
            print("Es 1")
        case 2:
            print("Es 2")
        case _:
            print("Otro valor")
