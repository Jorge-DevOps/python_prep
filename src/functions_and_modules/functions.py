if __name__ == "__main__":

##Funciones Integradas:

# abs(): Retorna el valor absoluto de un número.
# all(): Retorna True si todos los elementos de un iterable son True.
# Todos los elementos son verdaderos, entonces all() retorna True
    print(all([1, 2, 3]))  # True

    # Hay un elemento falso, entonces all() retorna False
    print(all([1, 2, 0]))  # False

    # El iterable está vacío, entonces all() retorna True
    print(all([]))  # True
# any(): Retorna True si al menos un elemento de un iterable es True.
   
    #Caso 1: Al menos un valor es verdadero:
    print(any([0, 1, 2, 3]))  # Devuelve True porque hay valores distintos de cero (1, 2, 3)
    #Caso 2: Todos los valores son falsos:
    print(any([0, 1, 2, 3]))  # Devuelve False porque todos los elementos son falsos

    #Caso 3: Usando una expresión generadora:
    print(any(x < 0 for x in [0, 1, 2, 3]))  # Devuelve True porque -2 es menor que 0


# bin(): Convierte un número entero a su representación binaria.
# bool(): Convierte un valor a su equivalente booleano (True o False).
# chr(): Convierte un número entero en su carácter Unicode.
# dict(): Crea un diccionario.
# dir(): Muestra los atributos y métodos de un objeto.
# divmod(): Retorna una tupla de dos elementos: el cociente y el residuo de la división.
# enumerate(): Devuelve un objeto enumerado (con índice) a partir de un iterable.
# eval(): Evalúa una expresión Python dentro de un string.
# exec(): Ejecuta dinámicamente el código Python pasado como string.
# filter(): Filtra elementos de un iterable que cumplen con una condición.
# float(): Convierte un valor a flotante.
# format(): Formatea cadenas de texto.
# frozenset(): Crea un conjunto inmutable.
# getattr(): Obtiene el valor de un atributo de un objeto.
# globals(): Devuelve el diccionario de todos los nombres globales.
# hasattr(): Verifica si un objeto tiene un atributo específico.
# hash(): Retorna el valor hash de un objeto.
# help(): Muestra la documentación de un objeto.
# hex(): Convierte un número a su representación hexadecimal.
# id(): Retorna el identificador único de un objeto.
# input(): Lee la entrada del usuario como una cadena.
# int(): Convierte un valor a entero.
# isinstance(): Verifica si un objeto es una instancia de una clase.
# issubclass(): Verifica si una clase es una subclase de otra.
# iter(): Retorna un iterador de un objeto iterable.
# len(): Retorna la longitud de un objeto.
# list(): Crea una lista.
# map(): Aplica una función a todos los elementos de un iterable.
# max(): Retorna el valor máximo de un iterable.
# min(): Retorna el valor mínimo de un iterable.
# next(): Retorna el siguiente elemento de un iterador.
# object(): Crea un objeto base.
# open(): Abre un archivo y devuelve un objeto de archivo.
# ord(): Convierte un carácter a su valor entero en Unicode.
# pow(): Calcula la potencia de un número.
# print(): Imprime en la consola.
# range(): Crea un iterable con una secuencia de números.
# repr(): Devuelve una cadena que representa a un objeto de manera exacta.
# reversed(): Retorna un iterador que recorre un objeto en orden inverso.
# round(): Redondea un número al número de decimales especificado.
# set(): Crea un conjunto.
# slice(): Crea un objeto de tipo "slice" (rebanado).
# sorted(): Devuelve una lista ordenada de un iterable.
# str(): Convierte un objeto a una cadena de texto.
# sum(): Calcula la suma de un iterable.
# tuple(): Crea una tupla.
# type(): Retorna el tipo de un objeto.
# zip(): Combina múltiples iterables en tuplas.

## Módulos estándar en Python:
#math: Proporciona funciones matemáticas avanzadas.
#random: Proporciona herramientas para generar números aleatorios.
#datetime: Proporciona clases para manejar fechas y horas.
#os: Proporciona funciones para interactuar con el sistema operativo.
#sys: Proporciona acceso a variables y funciones específicos del sistema.
#re: Proporciona soporte para expresiones regulares.
#json: Soporte para manejar datos JSON.
#pickle: Permite serializar y deserializar objetos Python.
#collections: Proporciona tipos de datos especializados como Counter, OrderedDict, etc.
#itertools: Funciones para manipular iteradores de manera eficiente.
#functools: Herramientas para trabajar con funciones de manera funcional.
#copy: Funciones para copiar objetos.
#subprocess: Permite ejecutar procesos externos.
#socket: Proporciona herramientas para la programación de redes.
#csv: Herramientas para leer y escribir archivos CSV.
#sqlite3: Permite interactuar con bases de datos SQLite.
#argparse: Permite crear interfaces de línea de comandos.
#logging: Permite registrar mensajes de log para depuración y monitoreo.
#threading: Proporciona soporte para la ejecución de múltiples hilos (threads).
#unittest: Proporciona un marco para realizar pruebas unitarias.