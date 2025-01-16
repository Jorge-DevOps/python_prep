# Tipos de datos en Python:

# 1. Tipos Numéricos:
# int: Números enteros.
# float: Números de punto flotante (decimales).
# complex: Números complejos (como 1 + 2j).

# 2. Secuencias:
# str: Cadenas de texto (strings).
# list: Listas, colecciones ordenadas y mutables de elementos.
my_list = [1, 2, 3, 4]
print(type(my_list))  # <class 'list'>

# tuple: Tuplas, colecciones ordenadas e inmutables de elementos.
my_tuple = (1, 2, 3)
print(type(my_tuple))  # <class 'tuple'>

# 3. Conjuntos (Sets):
# set: Conjuntos no ordenados de elementos únicos. Permiten realizar operaciones como uniones, intersecciones y diferencias.

# Unión: my_set | another_set
# Intersección: my_set & another_set
# Diferencia: my_set - another_set
# Diferencia simétrica: my_set ^ another_set

my_set = {1, 2, 3, 4, 5}
print(type(my_set))  # <class 'set'>


# frozenset: Versión inmutable de un conjunto (no se pueden agregar o quitar elementos después de la creación).
my_frozenset = frozenset([1, 2, 3, 4, 5])
print(type(my_frozenset))  # <class 'frozenset'>

# 4. Mapas:
# dict: Diccionarios, estructuras de datos que almacenan pares clave-valor. Las claves son únicas.
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(type(my_dict))  # <class 'dict'>

# 5. Tipos Booleanos:
# bool: Valores True o False, usados para lógica de control.

# 6. Tipos Binarios:
# bytes: Secuencias inmutables de bytes.
# bytearray: Secuencias mutables de bytes.
# memoryview: Permite ver y modificar los datos de objetos binarios sin copiarlos.

# 7. Tipos Especiales:
# None: Un tipo especial que representa la ausencia de valor o una referencia nula.
# Ejemplos:
# Set: Un conjunto en Python es una colección no ordenada de elementos únicos.


# Métodos:

# add(x): Agregar un elemento x.
# remove(x): Eliminar un elemento x, genera error si no existe.
# discard(x): Eliminar un elemento x, no genera error si no existe.
# pop(): Eliminar y retornar un elemento aleatorio.
# clear(): Eliminar todos los elementos del set.
# Resumen:
# Sets son una estructura de datos fundamental en Python para trabajar con colecciones de elementos únicos, y son muy útiles cuando necesitas realizar operaciones matemáticas como uniones, intersecciones, etc.