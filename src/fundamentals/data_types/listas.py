
# 1. Listas (List)
my_list = [1, 2, 3, "hello", 3.14]

# 2. Listas anidadas
nested_list = [[1, 2], [3, 4], [5, 6]]

# 3. Listas de comprensión
squares = [x**2 for x in range(10)]

# 4. Listas ordenadas (Sorted List)
sorted_list = sorted([3, 1, 4, 1, 5, 9])

# 5. Listas con duplicados
list_with_duplicates = [1, 2, 2, 3, 4, 4]

# 6. Listas vacías
empty_list = []

# 7. Listas con elementos de tipo único
integer_list = [1, 2, 3]
string_list = ["apple", "banana", "cherry"]

# 8. Listas circulares
## el diferencial de las listas circulares es su capacidad para comportarse de forma cíclica y mantener un tamaño constante, 
# lo que las hace útiles para tareas que requieren un procesamiento repetitivo de elementos de forma continua.
# circular_list.append(4)  # El primer elemento (1) se elimina y se agrega 4 al final
#Las listas circulares suelen tener un tamaño fijo

from collections import deque
circular_list = deque([1, 2, 3], maxlen=3)

# 9. Listas de tipo deque (Double-Ended Queue)
deque_list = deque([1, 2, 3])
deque_list.append(4)
deque_list.appendleft(0)

# 10. Tuplas como listas inmutables
my_tuple = (1, 2, 3)

# 11. Arrays (con el módulo array)
# array.array: Eficiente en memoria y optimizado para almacenar datos homogéneos de un tipo específico (como enteros o flotantes). 
# Ideal para grandes cantidades de datos numéricos.
# [] (listas): Más flexibles, pueden almacenar cualquier tipo de dato, pero no son tan eficientes para grandes volúmenes de datos homogéneos.
import array
arr = array.array('i', [1, 2, 3])
